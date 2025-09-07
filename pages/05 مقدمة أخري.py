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



st.markdown(
    """
    <p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
شهد عام 2024 استمرار تركز جهود المساعدات الإماراتية نحو التخفيف من حدة التداعيات للأزمات الإنسانية العالمية خاصة في المحيط الإقليمي، ويأتي في مقدمتها الأزمة الإنسانية في قطاع غزة والتي استحوذت على 23 في المائة من حجم المساعدات بقيمة 2.54 مليار درهم إماراتي (691 مليون دولار أمريكي) وبزيادة قدرها 20 في المئة مقارنة بعام 2023، ليصل اجمالي ما خصصته المساعدات الإماراتية للأزمة خلال العامين (2023-2024) مبلغ 4.65 مليار درهم اماراتي (1.27 مليار دولار أمريكي) بما يقارب خمس المساعدات خلال الفترة. وفي المرتبة الثانية جاءت المساعدات الموجهة نحو الازمة الإنسانية في السودان واليمن بنسب 9 في المئة تقريبا لكل منهما وبقيمة تزيد عن مليار درهم اماراتي (272 مليون دولار أمريكي). وبذلك استحوذت الأزمات الإنسانية الثلاث (قطاع غزة – السودان- اليمن) على أكثر من 40 في المئة من حجم المساعدات الإماراتية خلال العام 2024، بما يعكس الالتزام الراسخ من دولة الامارات نحو قيادة العمل الإنساني الدولي لمواجهة التحديات الإنسانية حول العالم، ودعم الجهود اللازمة للمساعي المبذولة لتخفيف المعاناة الإنسانية من تداعيات تلك الأزمات والكوارث‬‬.‬‬‬‬‬‬‬‬‬‬‬‬‬‬
    </p>
    """,
    unsafe_allow_html=True
)



# --- البيانات ---
data = """Country,Spending in 2022,Spending in 2023,Spending in 2024
Yemen Crisis (2015),90.82,161.99,276.65
Syria Crisis,42.29,40.31,82.9
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
# --- رسم الجراف ---
fig = px.line(
    df_long,
    x="Year",
    y="Spending",
    color="Country",
    markers=True,
    title="UAE Humanitarian Spending by Crisis (2022–2024)"
)

# ضبط المحور الأفقي بحيث يظهر فقط 2022–2023–2024
fig.update_layout(
    xaxis=dict(
        title="Year",
        categoryorder="array",
        categoryarray=["2022", "2023", "2024"]
    ),
    yaxis_title="Spending (Million USD)",
    hovermode="x unified"
)

# عرض على Streamlit
st.title("📊 Interactive Aid Spending Dashboard")
st.plotly_chart(fig, use_container_width=True)



















