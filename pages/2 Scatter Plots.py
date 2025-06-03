# uae_aid_dashboard/pages/2_Scatter_Plots.py
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
st.markdown("""
<style>
    /* General RTL and text alignment for the main content area */
    div.stApp {
        direction: rtl; /* Sets overall text direction to RTL */
        text-align: right; /* Aligns all text to the right by default */
    }

    /* Specific alignment for titles (h1, h2, h3) */
    h1, h2, h3, h4, h5, h6 {
        text-align: right; /* Ensures titles are right-aligned */
        direction: rtl;
    }

    /* Adjust Streamlit elements that might override general alignment */
    .stMarkdown, .stText, .stDataFrame, .stPlotlyChart, .stMetric, .stSelectbox, .stMultiSelect, .stRadio, .stSlider {
        text-align: right;
        direction: rtl;
    }

    /* Fix for sidebar elements alignment - some might need LTR context */
    /* This can be tricky, as Streamlit's sidebar elements are not always straightforward */
    /* If some elements appear misaligned, you might need to adjust them specifically */
    [data-testid="stSidebarContent"] {
        text-align: right; /* Aligns sidebar content to the right */
        direction: rtl;
    }

    /* Ensure specific elements like metric labels are right-aligned */
    [data-testid="stMetricLabel"] > div {
        width: 100%; /* Ensure the div takes full width */
        text-align: right; /* Align metric label to the right */
    }
    [data-testid="stMetricValue"] {
        text-align: right; /* Align metric value to the right */
    }
    [data-testid="stMetricDelta"] {
        text-align: right; /* Align metric delta to the right */
    }

    /* Adjust the general Streamlit container background (from previous theme setup) */
    .stApp {
        background-color: #f0f2f6; /* Light grey background */
    }
    /* Sidebar background (from previous theme setup) */
    [data-testid="stSidebar"] {
        background-color: #e0e0e0; /* Slightly darker grey for sidebar */
    }
    /* Header/Title color (from previous theme setup) */
    h1 {
        color: #004d40; /* Dark teal for main titles */
    }
    h2, h3 {
        color: #00695c; /* Slightly lighter teal for subtitles */
    }
    /* Primary button color (from previous theme setup) */
    .stButton>button {
        background-color: #00897b; /* Medium teal */
        color: white;
    }
    .stButton>button:hover {
        background-color: #00796b; /* Darker teal on hover */
    }
    /* Text color (from previous theme setup) */
    .css-1jc7ptx, .e16z5d4j0 { /* General text, often found in these classes */
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

st.title("📈 مخططات الانتشار للمساعدات الخارجية")
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

# Create the scatter plot
fig_scatter = px.scatter(filtered_df, **scatter_kwargs)
st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")
st.info("تم تطوير لوحة المعلومات هذه باستخدام Streamlit و Plotly. البيانات وهمية لأغراض العرض التوضيحي.")
