# uae_aid_dashboard/pages/1_Dashboard_Overview.py
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np # Add this import if not already present
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

st.title("📊 نظرة عامة على لوحة المعلومات")
st.markdown("هذه لوحة معلومات تفاعلية توضح اتجاهات المساعدات الخارجية لدولة الإمارات العربية المتحدة.")

# Sidebar for filters
st.sidebar.header("خيارات التصفية")
selected_years = st.sidebar.multiselect(
    "اختر السنوات:",
    options=df['Year'].unique().tolist(),
    default=df['Year'].unique().tolist()
)

filtered_df = df[df['Year'].isin(selected_years)]

if filtered_df.empty:
    st.warning("لا توجد بيانات للسنوات المختارة. يرجى تعديل التصفية.")
    st.stop()

# --- Overview Metrics ---
st.header("نظرة عامة على المقاييس الرئيسية")
col1, col2, col3 = st.columns(3)

with col1:
    total_aid_sum = filtered_df['Total Aid (AED Bn)'].sum()
    st.metric(label="إجمالي المساعدات (مليار درهم إماراتي)", value=f"{total_aid_sum:,.2f}")

with col2:
    oda_sum = filtered_df['ODA (AED Bn)'].sum()
    st.metric(label="المساعدة الإنمائية الرسمية (مليار درهم إماراتي)", value=f"{oda_sum:,.2f}")

with col3:
    avg_oda_gni = filtered_df['ODA as % of GNI'].mean()
    st.metric(label="متوسط المساعدة الإنمائية الرسمية كنسبة مئوية من الناتج القومي الإجمالي", value=f"{avg_oda_gni:.2%}")

st.markdown("---")

# --- Graphs and Charts ---

st.header("الرسوم البيانية التفاعلية")

# 1. Total Aid and ODA over Time
st.subheader("1. إجمالي المساعدات والمساعدة الإنمائية الرسمية بمرور الوقت")
fig1 = px.line(filtered_df, x='Date', y=['Total Aid (AED Bn)', 'ODA (AED Bn)'],
               title='إجمالي المساعدات والمساعدة الإنمائية الرسمية بمرور الوقت',
               labels={'value': 'القيمة (مليار درهم إماراتي)', 'Date': 'التاريخ'},
               line_shape='linear', hover_data={'Date': '|%Y-%m-%d'})
fig1.update_layout(hovermode="x unified")
st.plotly_chart(fig1, use_container_width=True)

# 2. ODA as % of GNI over Time
st.subheader("2. المساعدة الإنمائية الرسمية كنسبة مئوية من الناتج القومي الإجمالي بمرور الوقت")
fig2 = px.line(filtered_df, x='Date', y='ODA as % of GNI',
               title='المساعدة الإنمائية الرسمية كنسبة مئوية من الناتج القومي الإجمالي بمرور الوقت',
               labels={'ODA as % of GNI': 'النسبة المئوية', 'Date': 'التاريخ'},
               line_shape='linear', hover_data={'Date': '|%Y-%m-%d'})
fig2.update_layout(yaxis_tickformat=".2%", hovermode="x unified")
st.plotly_chart(fig2, use_container_width=True)

# 3. Aid Type Breakdown (Development, Humanitarian, Charitable) - Area Chart
st.subheader("3. تفصيل أنواع المساعدات (تنموية، إنسانية، خيرية)")
aid_type_cols = ['Development (%)', 'Humanitarian (%)', 'Charitable (%)']
df_aid_types = filtered_df.melt(id_vars=['Date', 'Year'], value_vars=aid_type_cols,
                                var_name='Aid Type', value_name='Percentage')
fig3 = px.area(df_aid_types, x='Date', y='Percentage', color='Aid Type',
               title='توزيع أنواع المساعدات بمرور الوقت',
               labels={'Percentage': 'النسبة المئوية', 'Date': 'التاريخ', 'Aid Type': 'نوع المساعدة'},
               hover_data={'Percentage': ':.2f%'})
fig3.update_layout(yaxis_tickformat=".2%")
st.plotly_chart(fig3, use_container_width=True)

# 4. Donor Contributions by Entity
st.subheader("4. مساهمات المانحين حسب الجهة")
donor_cols = ['Donor Contributions by Entity Govt (%)', 'Donor Contributions by Entity ADFD (%)', 'Donor Contributions by Entity ERC (%)']
# Calculate average contributions for pie chart
avg_donor_contributions = filtered_df[donor_cols].mean()

fig4 = px.pie(names=avg_donor_contributions.index, values=avg_donor_contributions.values,
              title='متوسط مساهمات المانحين حسب الجهة (%)',
              labels={'names': 'الجهة', 'values': 'متوسط النسبة المئوية'},
              hole=0.3)
fig4.update_traces(textinfo='percent+label')
st.plotly_chart(fig4, use_container_width=True)

# 5. Funding Type Breakdown (Grants vs Loans)
st.subheader("5. تفصيل نوع التمويل (منح مقابل قروض)")
funding_cols = ['Funding Type Breakdown Grants (%)', 'Funding Type Breakdown Loans (%)']
df_funding_types = filtered_df.melt(id_vars=['Date', 'Year'], value_vars=funding_cols,
                                    var_name='Funding Type', value_name='Percentage')
fig5 = px.bar(df_funding_types, x='Date', y='Percentage', color='Funding Type',
              title='توزيع أنواع التمويل بمرور الوقت',
              labels={'Percentage': 'النسبة المئوية', 'Date': 'التاريخ', 'Funding Type': 'نوع التمويل'},
              barmode='group', hover_data={'Percentage': ':.2f%'})
fig5.update_layout(yaxis_tickformat=".2%")
st.plotly_chart(fig5, use_container_width=True)

# 6. Aid by Modality (Bilateral vs Multilateral)
st.subheader("6. المساعدات حسب الوسيلة (ثنائية مقابل متعددة الأطراف)")
modality_cols = ['Aid by Modality Bilateral (%)', 'Aid by Modality Multilateral (%)']
df_modality_types = filtered_df.melt(id_vars=['Date', 'Year'], value_vars=modality_cols,
                                     var_name='Modality Type', value_name='Percentage')
fig6 = px.bar(df_modality_types, x='Date', y='Percentage', color='Modality Type',
              title='توزيع المساعدات حسب الوسيلة بمرور الوقت',
              labels={'Percentage': 'النسبة المئوية', 'Date': 'التاريخ', 'Modality Type': 'نوع الوسيلة'},
              barmode='stack', hover_data={'Percentage': ':.2f%'})
fig6.update_layout(yaxis_tickformat=".2%")
st.plotly_chart(fig6, use_container_width=True)

# 7. SDG Alignment (Top 5 SDGs)
st.subheader("7. توافق المساعدات مع أهداف التنمية المستدامة")
sdg_cols = [col for col in df.columns if 'SDG Alignment' in col]
# Calculate average for each SDG over the filtered period
avg_sdg_alignment = filtered_df[sdg_cols].mean().sort_values(ascending=False).head(5) # Top 5 SDGs

fig7 = px.bar(x=avg_sdg_alignment.index, y=avg_sdg_alignment.values,
              title='متوسط توافق المساعدات مع أهداف التنمية المستدامة (أعلى 5)',
              labels={'x': 'هدف التنمية المستدامة', 'y': 'متوسط النسبة المئوية'},
              color=avg_sdg_alignment.values, color_continuous_scale=px.colors.sequential.Viridis)
fig7.update_layout(yaxis_tickformat=".2%")
st.plotly_chart(fig7, use_container_width=True)

# 8. Spending by Sector (Top 7 Sectors)
st.subheader("8. الإنفاق حسب القطاع")
sector_cols = [col for col in df.columns if 'Spending by Sector' in col]
# Calculate average for each sector over the filtered period
avg_sector_spending = filtered_df[sector_cols].mean().sort_values(ascending=False).head(7) # Top 7 Sectors

fig8 = px.bar(x=avg_sector_spending.index, y=avg_sector_spending.values,
              title='متوسط الإنفاق حسب القطاع (أعلى 7 قطاعات)',
              labels={'x': 'القطاع', 'y': 'متوسط النسبة المئوية'},
              color=avg_sector_spending.values, color_continuous_scale=px.colors.sequential.Plasma)
fig8.update_layout(yaxis_tickformat=".2%")
st.plotly_chart(fig8, use_container_width=True)


# 9. Top Recipient Countries - Bar Chart
st.subheader("9. أكبر الدول المستفيدة")
# Count occurrences of each top recipient country in the filtered data
top_recipient_counts = filtered_df['Top Recipient Country'].value_counts().reset_index()
top_recipient_counts.columns = ['Country', 'Count']

fig9 = px.bar(top_recipient_counts, x='Country', y='Count',
              title='تكرار ظهور الدول المستفيدة الأعلى',
              labels={'Country': 'البلد', 'Count': 'عدد مرات الظهور كأكبر مستفيد'},
              color='Count', color_continuous_scale=px.colors.sequential.RdBu)
st.plotly_chart(fig9, use_container_width=True)

st.markdown("---")
st.info("تم تطوير لوحة المعلومات هذه باستخدام Streamlit و Plotly. البيانات وهمية لأغراض العرض التوضيحي.")
