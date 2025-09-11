import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO


st.set_page_config(    layout="wide",    page_title="UAE Foreign Aid Hub",    page_icon="🇦🇪",    initial_sidebar_state="expanded")

st.markdown("""
<style>
    div.stApp {
        direction: rtl;
        text-align: right;
        background-color: #f0f2f6; /* Light grey background */
    }

    h1 {
        color: #004d40; /* Dark teal */
        text-align: right;
    }
    h2, h3 {
        color: #00695c; /* Slightly lighter teal */
        text-align: right;
    }

    [data-testid="stSidebar"] {
        background-color: #e0e0e0; /* Sidebar color */
        direction: rtl;
        text-align: right;
    }

    /* Fix alignment for sidebar content */
    [data-testid="stSidebarContent"] {
        text-align: right;
        direction: rtl;
    }

    /* Center images */
    .stImage {
        display: flex;
        justify-content: center;
    }

    /* Buttons */
    .stButton>button {
        background-color: #00897b;
        color: white;
    }
    .stButton>button:hover {
        background-color: #00796b;
    }

    /* Text color */
    .css-1jc7ptx, .e16z5d4j0 {
        color: #263238;
    }
</style>
""", unsafe_allow_html=True)

 


st.title("بيانات عامة")




st.set_page_config(layout="wide")

# --- البيانات ---
data = """Country,Spending in 2022,Spending in 2023,Spending in 2024
Yemen Crisis (2015),90.82,161.99,276.65
Gaza conflict (2023),0.0,574.72,691.32
Sudan conflict (2023),0.0,123.63,276.77
"""

# قراءة البيانات
df = pd.read_csv(StringIO(data))

# تحويل البيانات من Wide إلى Long لتسهيل الرسم
df_long = df.melt(id_vars="Country", 
                  var_name="Year", 
                  value_name="Spending")

# تنظيف أسماء السنوات
df_long["Year"] = df_long["Year"].str.replace("Spending in ", "")

# تقسيم الصفحة لعمودين (يمين لزر اختيار السنة، شمال للجراف)
col1, col2 = st.columns([1, 3])

with col1:
    selected_year = st.radio(
        "📅 اختر السنة:",
        options=sorted(df_long["Year"].unique()),
        index=0,
        key="year_selector"
    )

# فلترة البيانات على السنة المختارة
filtered_df = df_long[df_long["Year"] == selected_year]
 
# رسم الجراف
fig = px.bar(
    filtered_df,
    x="Country",
    y="Spending",
    text="Spending",
    color="Country",
    title=f"📊 الدعم الإنساني للأزمات والكوارث في {selected_year}",
    height=500
)

# تحسين الشكل
fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
fig.update_layout(
    xaxis_title="Country",
    yaxis_title="Spending (Million USD)",
    showlegend=False,
    width=800,
    margin=dict(l=20, r=20, t=60, b=20)
)

with col2:
    st.plotly_chart(fig, use_container_width=False)


##################################################

 


# --- النص التوضيحي ---
col1, col2, col3 = st.columns([1,2,1])  # العمود الأوسط أوسع

# --- البيانات ---
data = """Category,Spending in 2022,Spending in 2023,Spending in 2024
Humanitarian,435.86,1334.84,1149.3
Development,2858.41,1718.77,1785.54
Charity,154.85,124.62,131.55
"""

# قراءة البيانات
df = pd.read_csv(StringIO(data))

# تحويل البيانات من Wide إلى Long
df_long = df.melt(
    id_vars="Category", 
    var_name="Year", 
    value_name="Spending"
)

# تنظيف أسماء السنوات
df_long["Year"] = df_long["Year"].str.replace("Spending in ", "")

# --- رسم الجراف الجديد (Grouped Bar Chart) ---
fig = px.bar(
    df_long,
    x="Year",
    y="Spending",
    color="Category",
    barmode="group",  # يعرض كل فئة بجانب الأخرى للسنة نفسها
    text="Spending",
    title="💰 توزيع المساعدات الإماراتية حسب الفئة (2022 – 2024)"
)

fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")

fig.update_layout(
    xaxis=dict(
        title="السنة",
        categoryorder="array",
        categoryarray=["2022", "2023", "2024"]
    ),
    yaxis_title="Spending (Million USD)",
    hovermode="x unified",
    width=800, height=500,
    legend=dict(title="الفئة")
)

# نخلي الرسم في منتصف الصفحة
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.plotly_chart(fig, use_container_width=False)






st.markdown(
    """
    <p style='color:#5d6063; font-size:25px; font-weight:bold; text-align:center;'>
    🎯 اختر السنة لعرض النسب المئوية للفئات
    </p>
    """,
    unsafe_allow_html=True
)

# --- البيانات ---
data = {
    "Category": ["Humanitarian", "Development", "Charity"],
    "2022": [435.86, 2858.41, 154.85],
    "2023": [1334.84, 1718.77, 124.62],
    "2024": [1149.3, 1785.54, 131.55]
}
df = pd.DataFrame(data)

# --- اختيار السنة من اليمين ---
col1, col2 = st.columns([1, 3])
with col1:
    selected_year = st.radio("اختر السنة:", ["2022", "2023", "2024"], index=2)

# --- رسم الجراف ---
fig = px.pie(
    df,
    values=selected_year,
    names="Category",
    title=f"النسب المئوية للإنفاق في {selected_year}",
    hole=0.4  # لعمل Donut Chart
)

fig.update_traces(
    textinfo="percent+label",
    pull=[0.05, 0.05, 0.05]  # لسحب القطاعات للخارج قليلاً لزيادة الوضوح
)

fig.update_layout(
    width=500,
    height=500,
    title_x=0.5,
    title_font=dict(size=22)
)

with col2:
    st.plotly_chart(fig, use_container_width=False)
















