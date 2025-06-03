# uae_aid_dashboard/pages/5_Bar_Charts.py
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

st.title("📊 رسوم بيانية عمودية (Bar Charts)")
st.markdown("استكشف المقارنات عبر الفئات المختلفة للمساعدات الخارجية.")

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

chart_options = {
    "أكبر الدول المستفيدة (عدد مرات الظهور)": "Top Recipient Country",
    "متوسط الإنفاق حسب القطاع": [col for col in df.columns if 'Spending by Sector' in col],
    "متوسط توافق أهداف التنمية المستدامة": [col for col in df.columns if 'SDG Alignment' in col],
    "متوسط مساهمات الجهات المانحة": ['Donor Contributions by Entity Govt (%)', 'Donor Contributions by Entity ADFD (%)', 'Donor Contributions by Entity ERC (%)'],
}

selected_chart_type = st.sidebar.selectbox(
    "اختر نوع الرسم البياني العمودي:",
    options=list(chart_options.keys())
)

st.markdown("---")

# --- Bar Chart Display ---
st.header(selected_chart_type)

if selected_chart_type == "أكبر الدول المستفيدة (عدد مرات الظهور)":
    top_recipient_counts = filtered_df['Top Recipient Country'].value_counts().reset_index()
    top_recipient_counts.columns = ['Country', 'Count']
    fig_bar = px.bar(top_recipient_counts, x='Country', y='Count',
                     title='تكرار ظهور الدول المستفيدة الأعلى',
                     labels={'Country': 'البلد', 'Count': 'عدد مرات الظهور كأكبر مستفيد'},
                     color='Count', color_continuous_scale=px.colors.sequential.RdBu)
elif selected_chart_type == "متوسط الإنفاق حسب القطاع":
    sector_cols = chart_options[selected_chart_type]
    avg_sector_spending = filtered_df[sector_cols].mean().sort_values(ascending=False)
    # Clean up labels for display
    labels = [col.replace('Spending by Sector ', '') for col in avg_sector_spending.index]
    fig_bar = px.bar(x=labels, y=avg_sector_spending.values,
                     title='متوسط الإنفاق حسب القطاع',
                     labels={'x': 'القطاع', 'y': 'متوسط النسبة المئوية'},
                     color=avg_sector_spending.values, color_continuous_scale=px.colors.sequential.Plasma)
    fig_bar.update_layout(yaxis_tickformat=".2%")
elif selected_chart_type == "متوسط توافق أهداف التنمية المستدامة":
    sdg_cols = chart_options[selected_chart_type]
    avg_sdg_alignment = filtered_df[sdg_cols].mean().sort_values(ascending=False)
    # Clean up labels for display
    labels = [col.replace('SDG Alignment ', '') for col in avg_sdg_alignment.index]
    fig_bar = px.bar(x=labels, y=avg_sdg_alignment.values,
                     title='متوسط توافق المساعدات مع أهداف التنمية المستدامة',
                     labels={'x': 'هدف التنمية المستدامة', 'y': 'متوسط النسبة المئوية'},
                     color=avg_sdg_alignment.values, color_continuous_scale=px.colors.sequential.Viridis)
    fig_bar.update_layout(yaxis_tickformat=".2%")
elif selected_chart_type == "متوسط مساهمات الجهات المانحة":
    donor_cols = chart_options[selected_chart_type]
    avg_donor_contributions = filtered_df[donor_cols].mean()
    # Clean up labels for display
    labels = [col.replace('Donor Contributions by Entity ', '')
              .replace(' (%)', '') for col in avg_donor_contributions.index]
    fig_bar = px.bar(x=labels, y=avg_donor_contributions.values,
                     title='متوسط مساهمات المانحين حسب الجهة',
                     labels={'x': 'الجهة المانحة', 'y': 'متوسط النسبة المئوية'},
                     color=avg_donor_contributions.values, color_continuous_scale=px.colors.sequential.Teal)
    fig_bar.update_layout(yaxis_tickformat=".2%")


if 'fig_bar' in locals(): # Check if a figure was created
    st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.warning("لا توجد بيانات كافية لإنشاء الرسم البياني العمودي للفئة المختارة في السنوات المحددة.")

st.markdown("---")
st.info("تم تطوير لوحة المعلومات هذه باستخدام Streamlit و Plotly. البيانات وهمية لأغراض العرض التوضيحي.")
