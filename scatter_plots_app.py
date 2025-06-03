import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(
    layout="wide",
    page_title="UAE Foreign Aid Scatter Plots",
    page_icon="📈",
    initial_sidebar_state="expanded"
)

# --- Streamlit Theme Customization (consistent with previous app) ---
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6; /* Light grey background */
    }
    [data-testid="stSidebar"] {
        background-color: #e0e0e0; /* Slightly darker grey for sidebar */
    }
    h1 {
        color: #004d40; /* Dark teal for main titles */
    }
    h2, h3 {
        color: #00695c; /* Slightly lighter teal for subtitles */
    }
    .stButton>button {
        background-color: #00897b; /* Medium teal */
        color: white;
    }
    .stButton>button:hover {
        background-color: #00796b; /* Darker teal on hover */
    }
    .css-1jc7ptx, .e16z5d4j0 {
        color: #263238; /* Dark grey for general text */
    }
</style>
""", unsafe_allow_html=True)

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('uae_foreign_aid_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    return df

df = load_data()

st.title("📈 لوحة معلومات مخططات الانتشار للمساعدات الخارجية لدولة الإمارات")
st.markdown("استكشف العلاقات بين مقاييس المساعدات الخارجية المختلفة.")

# --- Sidebar for Filters and X/Y Axis Selection ---
st.sidebar.header("خيارات المخطط")

selected_years = st.sidebar.multiselect(
    "اختر السنوات:",
    options=df['Year'].unique().tolist(),
    default=df['Year'].unique().tolist()
)

filtered_df = df[df['Year'].isin(selected_years)]

if filtered_df.empty:
    st.warning("لا توجد بيانات للسنوات المختارة. يرجى تعديل التصفية.")
    st.stop()

# Get all numeric columns for X and Y axis selection
numeric_cols = filtered_df.select_dtypes(include=np.number).columns.tolist()

# Remove date/time related numerical columns that don't make sense for scatter plot axes
# You might need to adjust this list based on your specific data
exclude_cols = ['Year', 'Month']
numeric_cols = [col for col in numeric_cols if col not in exclude_cols]

x_axis = st.sidebar.selectbox("المحور السيني (X-Axis):", options=numeric_cols, index=numeric_cols.index('Total Aid (AED Bn)'))
y_axis = st.sidebar.selectbox("المحور الصادي (Y-Axis):", options=numeric_cols, index=numeric_cols.index('ODA (AED Bn)'))
color_by = st.sidebar.selectbox("اللون حسب (Color By):", options=['None'] + df.columns.tolist())
size_by = st.sidebar.selectbox("الحجم حسب (Size By):", options=['None'] + numeric_cols)
hover_name = st.sidebar.selectbox("اسم التمرير (Hover Name):", options=['None', 'Date', 'Top Recipient Country'])

st.markdown("---")

# --- Scatter Plot ---
st.header(f"مخطط الانتشار: {y_axis} مقابل {x_axis}")

# Prepare kwargs for px.scatter based on user selections
scatter_kwargs = {
    'x': x_axis,
    'y': y_axis,
    'title': f'{y_axis} مقابل {x_axis}',
    'labels': {x_axis: x_axis, y_axis: y_axis},
    'hover_name': hover_name if hover_name != 'None' else None,
    'hover_data': {'Date': '|%Y-%m-%d'} if 'Date' in filtered_df.columns else None
}

if color_by != 'None':
    if color_by in numeric_cols:
        scatter_kwargs['color'] = color_by
        scatter_kwargs['color_continuous_scale'] = px.colors.sequential.Viridis
    else: # Categorical column
        scatter_kwargs['color'] = color_by

if size_by != 'None':
    scatter_kwargs['size'] = size_by
    # Adjust size scaling if desired, e.g., size_max=60

# Create the scatter plot
fig_scatter = px.scatter(filtered_df, **scatter_kwargs)
st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")
st.info("تم تطوير لوحة المعلومات هذه باستخدام Streamlit و Plotly. البيانات وهمية لأغراض العرض التوضيحي.")