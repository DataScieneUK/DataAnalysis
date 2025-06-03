# uae_aid_dashboard/pages/4_Histograms.py
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

st.title("📊 رسوم بيانية توزيعية (Histograms)")
st.markdown("استكشف توزيع قيم المتغيرات المختلفة للمساعدات الخارجية.")

# --- Sidebar for Filters and Column Selection ---
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

# Get all numeric columns for histogram selection
numeric_cols = filtered_df.select_dtypes(include=np.number).columns.tolist()
exclude_cols = ['Year', 'Month'] # Exclude non-meaningful numeric cols for distribution
numeric_cols = [col for col in numeric_cols if col not in exclude_cols]

if not numeric_cols:
    st.warning("لا توجد أعمدة رقمية قابلة للتحليل في البيانات المحددة.")
    st.stop()

column_to_plot = st.sidebar.selectbox("اختر المتغير لعرض التوزيع:", options=numeric_cols)

st.markdown("---")

# --- Histogram Display ---
st.header(f"توزيع: {column_to_plot}")

# Determine number of bins for the histogram
num_bins = st.sidebar.slider("عدد الفئات (Bins):", min_value=10, max_value=100, value=30)

fig_hist = px.histogram(filtered_df, x=column_to_plot, nbins=num_bins,
                        title=f'توزيع {column_to_plot}',
                        labels={column_to_plot: column_to_plot, 'count': 'العدد/التكرار'},
                        color_discrete_sequence=px.colors.qualitative.Plotly) # Use a nice color scheme
st.plotly_chart(fig_hist, use_container_width=True)

st.markdown("---")
st.info("تم تطوير لوحة المعلومات هذه باستخدام Streamlit و Plotly. البيانات وهمية لأغراض العرض التوضيحي.")
