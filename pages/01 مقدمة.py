

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



# st.markdown(
#     """
#     <p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
# شهد عام 2024 استمرار تركز جهود المساعدات الإماراتية نحو التخفيف من حدة التداعيات للأزمات الإنسانية العالمية خاصة في المحيط الإقليمي، ويأتي في مقدمتها الأزمة الإنسانية في قطاع غزة والتي استحوذت على 23 في المائة من حجم المساعدات بقيمة 2.54 مليار درهم إماراتي (691 مليون دولار أمريكي) وبزيادة قدرها 20 في المئة مقارنة بعام 2023، ليصل اجمالي ما خصصته المساعدات الإماراتية للأزمة خلال العامين (2023-2024) مبلغ 4.65 مليار درهم اماراتي (1.27 مليار دولار أمريكي) بما يقارب خمس المساعدات خلال الفترة. وفي المرتبة الثانية جاءت المساعدات الموجهة نحو الازمة الإنسانية في السودان واليمن بنسب 9 في المئة تقريبا لكل منهما وبقيمة تزيد عن مليار درهم اماراتي (272 مليون دولار أمريكي). وبذلك استحوذت الأزمات الإنسانية الثلاث (قطاع غزة – السودان- اليمن) على أكثر من 40 في المئة من حجم المساعدات الإماراتية خلال العام 2024، بما يعكس الالتزام الراسخ من دولة الامارات نحو قيادة العمل الإنساني الدولي لمواجهة التحديات الإنسانية حول العالم، ودعم الجهود اللازمة للمساعي المبذولة لتخفيف المعاناة الإنسانية من تداعيات تلك الأزمات والكوارث‬‬.‬‬‬‬‬‬‬‬‬‬‬‬‬‬
#     </p>
#     """,
#     unsafe_allow_html=True
# )



# # --- البيانات ---
# data = """Country,Spending in 2022,Spending in 2023,Spending in 2024
# Yemen Crisis (2015),90.82,161.99,276.65
# Gaza conflict (2023),0.0,574.72,691.32
# Sudan conflict (2023),0.0,123.63,276.77
# """

# # قراءة البيانات
# df = pd.read_csv(StringIO(data))

# # تحويل البيانات من Wide إلى Long لتسهيل الرسم
# df_long = df.melt(id_vars="Country", 
#                   var_name="Year", 
#                   value_name="Spending")

# # تنظيف أسماء السنوات
# df_long["Year"] = df_long["Year"].str.replace("Spending in ", "")

# # --- رسم الجراف ---
# fig = px.line(
#     df_long,
#     x="Year",
#     y="Spending",
#     color="Country",
#     markers=True,
#     title="الدعم الإنساني للإمارات للأزمات و الكوارث (2022–2024)"
# )

# # تعديل الشكل
# fig.update_layout(xaxis_title="Year",    yaxis_title="Spending (Million USD)",    hovermode="x unified",width=800, height=500)




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
    st.plotly_chart(fig, use_container_width=True)











st.markdown(
    """
    <p style='color:#5d6063; font-size:25px; font-weight:bold; text-align:justify;'>
📊 المساعدات الإنسانية علي مدار السنوات الثلاثة الماضية
    </p>
    """,
    unsafe_allow_html=True
)


# نخلي الرسم في منتصف الصفحة
col1, col2, col3 = st.columns([1,2,1])  # العمود الأوسط أوسع
with col2:
    st.plotly_chart(fig, use_container_width=False)


# st.plotly_chart(fig, use_container_width=True)



st.markdown(
    """
    <p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
بلغ إجمالي قيمة المساعدات الخارجية لدولة الإمارات خلال عام 2024 مبلغ 11.26 مليار درهم (3.07 مليار دولار أمريكي). 
وتشمل المساعدات مجموعة متنوعة من الفئات، تم تصنيفها لأغراض التوثيق والتحليل والتوافق مع المعايير الدولية لتتبع وتسجيل المساعدات إلى ثلاث فئات رئيسية: المساعدات الإنسانية، والمساعدات التنموية، والمساعدات الخيرية. 
    </p>
    """,
    unsafe_allow_html=True
)



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

# --- رسم الجراف ---
fig = px.line(
    df_long,
    x="Year",
    y="Spending",
    color="Category",
    markers=True,
    title="الدعم الإنساني للإمارات عبر النوع (2022–2024)"
)

# ضبط المحور الأفقي بحيث يظهر فقط 2022–2023–2024
fig.update_layout(
    xaxis=dict(
        title="Year",
        categoryorder="array",
        categoryarray=["2022", "2023", "2024"]
    ),
    yaxis_title="Spending (Million USD)",
    hovermode="x unified",
    width=800, height=500
)
 



st.markdown(
    """
    <p style='color:#5d6063; font-size:25px; font-weight:bold; text-align:justify;'>
📊 أنواع المساعدات الإنسانية علي مدار السنوات الثلاثة الماضية
    </p>
    """,
    unsafe_allow_html=True
)



# st.plotly_chart(fig, use_container_width=True)


#fig.update_traces(textposition="outside")
#fig.update_layout(width=600, height=500)  # 👈 عرض أقل

# # نخلي الرسم في منتصف الصفحة
col1, col2, col3 = st.columns([1,2,1])  # العمود الأوسط أوسع
with col2:
    st.plotly_chart(fig, use_container_width=False)



st.markdown(
    """
    <p style='color:#5d6063; font-size:25px; font-weight:bold; text-align:justify;'>
و هنا لعرض النسب المئوية
    </p>
    """,
    unsafe_allow_html=True
)




# البيانات
data = {
    "Category": ["Humanitarian", "Development", "Charity"],
    "2022": [435.86, 2858.41, 154.85],
    "2023": [1334.84, 1718.77, 124.62],
    "2024": [1149.3, 1785.54, 131.55]
}

df = pd.DataFrame(data)

# إنشاء الأعمدة لعرض 3 جرافات جنب بعض
col1, col2, col3 = st.columns(3)

with col1:
    fig_2022 = px.pie(df, values="2022", names="Category", 
                      title="إنفاق عام 2022 (%)")
    st.plotly_chart(fig_2022, use_container_width=True)

with col2:
    fig_2023 = px.pie(df, values="2023", names="Category", 
                      title="إنفاق عام 2023 (%)")
    st.plotly_chart(fig_2023, use_container_width=True)

with col3:
    fig_2024 = px.pie(df, values="2024", names="Category", 
                      title="إنفاق عام 2024 (%)")
    st.plotly_chart(fig_2024, use_container_width=True)


























