# uae_aid_dashboard/pages/4_Histograms.py
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