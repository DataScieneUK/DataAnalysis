# uae_aid_dashboard/pages/3_Pie_Charts.py
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

st.title("📊 المخططات الدائرية للمساعدات الخارجية")
st.markdown("تحليل توزيع المساعدات الخارجية الإماراتية عبر قطاعات وفئات مختلفة.")

# --- Sidebar for Filters and Chart Selection ---
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

# Define categories for pie charts
pie_chart_categories = {
    "Donor Contributions by Entity": ['Donor Contributions by Entity Govt (%)', 'Donor Contributions by Entity ADFD (%)', 'Donor Contributions by Entity ERC (%)'],
    "Funding Type Breakdown": ['Funding Type Breakdown Grants (%)', 'Funding Type Breakdown Loans (%)'],
    "Aid by Modality": ['Aid by Modality Bilateral (%)', 'Aid by Modality Multilateral (%)'],
    "SDG Alignment (Top 5)": [col for col in df.columns if 'SDG Alignment' in col],
    "Spending by Sector (Top 7)": [col for col in df.columns if 'Spending by Sector' in col],
    "Aid Type Breakdown": ['Development (%)', 'Humanitarian (%)', 'Charitable (%)']
}

chart_selection = st.sidebar.selectbox(
    "اختر فئة المخطط الدائري:",
    options=list(pie_chart_categories.keys())
)

st.markdown("---")

# --- Pie Chart Display ---
st.header(f"توزيع: {chart_selection}")

cols_to_plot = pie_chart_categories[chart_selection]

# Handle dynamic top N for SDG and Sector
if chart_selection == "SDG Alignment (Top 5)":
    avg_values = filtered_df[cols_to_plot].mean().sort_values(ascending=False).head(5)
    labels = [col.replace('SDG Alignment ', '') for col in avg_values.index]
    values = avg_values.values
    chart_title = "متوسط توافق المساعدات مع أهداف التنمية المستدامة (أعلى 5)"
elif chart_selection == "Spending by Sector (Top 7)":
    avg_values = filtered_df[cols_to_plot].mean().sort_values(ascending=False).head(7)
    labels = [col.replace('Spending by Sector ', '') for col in avg_values.index]
    values = avg_values.values
    chart_title = "متوسط الإنفاق حسب القطاع (أعلى 7 قطاعات)"
else:
    # For other categories, simply average the percentages over the filtered period
    avg_values = filtered_df[cols_to_plot].mean()
    labels = [col.replace('Donor Contributions by Entity ', '')
              .replace('Funding Type Breakdown ', '')
              .replace('Aid by Modality ', '')
              .replace(' (%)', '')
              for col in avg_values.index]
    values = avg_values.values
    chart_title = f"متوسط توزيع {chart_selection}"


if not np.all(np.isnan(values)) and np.sum(values) > 0: # Check if there are valid values to plot
    fig_pie = px.pie(names=labels, values=values,
                     title=chart_title,
                     labels={'names': 'الفئة', 'values': 'متوسط النسبة المئوية'},
                     hole=0.4) # Donut chart
    fig_pie.update_traces(textinfo='percent+label', pull=[0.05] * len(labels)) # Pull slices slightly for emphasis
    st.plotly_chart(fig_pie, use_container_width=True)
else:
    st.warning("لا توجد بيانات كافية لإنشاء المخطط الدائري للفئة المختارة في السنوات المحددة.")

st.markdown("---")
st.info("تم تطوير لوحة المعلومات هذه باستخدام Streamlit و Plotly. البيانات وهمية لأغراض العرض التوضيحي.")
