# uae_aid_dashboard/pages/6_Distributions.py
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('uae_foreign_aid_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    return df

df = load_data()

st.title("📊 الرسوم البيانية التوزيعية المتقدمة")
st.markdown("استكشف توزيعات البيانات المتعمقة باستخدام مخططات الصندوق (Box Plots) ومخططات الكمان (Violin Plots).")

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

# Get all numeric columns for distribution plots
numeric_cols = filtered_df.select_dtypes(include=np.number).columns.tolist()
exclude_cols = ['Year', 'Month']
numeric_cols = [col for col in numeric_cols if col not in exclude_cols]

if not numeric_cols:
    st.warning("لا توجد أعمدة رقمية قابلة للتحليل في البيانات المحددة.")
    st.stop()

column_to_analyze = st.sidebar.selectbox("اختر المتغير لتحليل توزيعه:", options=numeric_cols)
chart_type = st.sidebar.radio("اختر نوع المخطط:", ('Box Plot', 'Violin Plot'))
group_by_category = st.sidebar.selectbox(
    "التجميع حسب فئة (اختياري):",
    options=['None', 'Year', 'Top Recipient Country']
)

st.markdown("---")

# --- Distribution Plots Display ---
st.header(f"تحليل التوزيع لـ: {column_to_analyze}")

if chart_type == 'Box Plot':
    if group_by_category != 'None':
        fig_dist = px.box(filtered_df, x=group_by_category, y=column_to_analyze,
                          title=f'توزيع {column_to_analyze} حسب {group_by_category}',
                          labels={column_to_analyze: column_to_analyze, group_by_category: group_by_category},
                          color=group_by_category,
                          color_discrete_sequence=px.colors.qualitative.Bold)
    else:
        fig_dist = px.box(filtered_df, y=column_to_analyze,
                          title=f'توزيع {column_to_analyze}',
                          labels={column_to_analyze: column_to_analyze},
                          color_discrete_sequence=px.colors.qualitative.Bold)
elif chart_type == 'Violin Plot':
    if group_by_category != 'None':
        fig_dist = px.violin(filtered_df, x=group_by_category, y=column_to_analyze,
                             title=f'توزيع {column_to_analyze} حسب {group_by_category}',
                             labels={column_to_analyze: column_to_analyze, group_by_category: group_by_category},
                             color=group_by_category, box=True, # Show internal box plots
                             color_discrete_sequence=px.colors.qualitative.Vivid)
    else:
        fig_dist = px.violin(filtered_df, y=column_to_analyze,
                             title=f'توزيع {column_to_analyze}',
                             labels={column_to_analyze: column_to_analyze},
                             box=True, # Show internal box plot
                             color_discrete_sequence=px.colors.qualitative.Vivid)

st.plotly_chart(fig_dist, use_container_width=True)

st.markdown("---")
st.info("تم تطوير لوحة المعلومات هذه باستخدام Streamlit و Plotly. البيانات وهمية لأغراض العرض التوضيحي.")