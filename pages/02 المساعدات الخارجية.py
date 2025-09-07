import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config (لازم يكون أول حاجة) ---
st.set_page_config(
    layout="wide",
    page_title="UAE Foreign Aid Hub",
    page_icon="🇦🇪",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for RTL, colors, and centering images ---
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


# --- Content ---
st.title("المساعدات الخارجية")

#st.subheader(    "في عام 2024، ركزت المساعدات الخارجية لدولة الإمارات على خمسة أهداف رئيسية من أهداف التنمية المستدامة، شكلت مجتمعة أكثر من 84 في المئة من إجمالي المساعدات الموجهة لدعم القضايا العالمية الملحّة.")

st.markdown(
    """
    <p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
    في عام 2024، ركزت المساعدات الخارجية لدولة الإمارات على خمسة أهداف رئيسية من أهداف التنمية المستدامة، 
    شكلت مجتمعة أكثر من 84 في المئة من إجمالي المساعدات الموجهة لدعم القضايا العالمية الملحّة.
    </p>
    """,
    unsafe_allow_html=True
)



# البيانات
data = {
    "Goal": ["Goal 1", "Goal 17", "Goal 3", "Goal 11", "Goal 2"],
    "2022": [11.02, 51.26, 11.84, 7.92, 6.66],
    "2023": [28.67, 17.85, 9.84, 10.65, 12.76],
    "2024": [26.40, 21.51, 17.27, 9.80, 8.97]
}

df = pd.DataFrame(data)

# أعمدة لعرض الرسومات جنب بعض
col1, col2, col3 = st.columns(3)

with col1:
    fig_2022 = px.bar(df, x="Goal", y="2022", 
                      title="النسب المؤية للإنفاق عبر الأهداف في 2022 (%)",
                      text="2022",
                      color="Goal")
    fig_2022.update_traces(textposition="outside")
    st.plotly_chart(fig_2022, use_container_width=True)

with col2:
    fig_2023 = px.bar(df, x="Goal", y="2023", 
                      title="النسب المؤية للإنفاق عبر الأهداف في 2023 (%)",
                      text="2023",
                      color="Goal")
    fig_2023.update_traces(textposition="outside")
    st.plotly_chart(fig_2023, use_container_width=True)

with col3:
    fig_2024 = px.bar(df, x="Goal", y="2024", 
                      title="النسب المؤية للإنفاق عبر الأهداف في 2024 (%)",
                      text="2024",
                      color="Goal")
    fig_2024.update_traces(textposition="outside")
    st.plotly_chart(fig_2024, use_container_width=True)

#st.subheader(    "شكلت المنح النسبة الأكبر من تقديم المساعدات الخارجية الإماراتية في عام 2024، بنسبة 78.7 في المئة من الإجمالي، مبلغ 8.87 مليار درهم إماراتي (2.4 مليار دولار أمريكي). وقد استفادت من هذه المنح 133 دولة، من بينها 38 دولة مصنفة ضمن أقل البلدان نمواً. حيث حصلت فلسطين على الحصة الأكبر بقيمة 2.62 مليار درهم إماراتي (712.89 مليون دولار أمريكي)، ما يمثل نسبة 29.5 في المئة من إجمالي المنح، تلتها اليمن بمبلغ 1.02 مليار درهم إماراتي (277.12 مليون دولار أمريكي) ما يمثل نسبة 11.5 في المئة من إجمالي المنح.")


st.markdown(
    """
    <p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
    شكلت المنح النسبة الأكبر من تقديم المساعدات الخارجية الإماراتية في عام 2024، بنسبة 78.7 في المئة من الإجمالي، مبلغ 8.87 مليار درهم إماراتي (2.4 مليار دولار أمريكي). وقد استفادت من هذه المنح 133 دولة، من بينها 38 دولة مصنفة ضمن أقل البلدان نمواً. حيث حصلت فلسطين على الحصة الأكبر بقيمة 2.62 مليار درهم إماراتي (712.89 مليون دولار أمريكي)، ما يمثل نسبة 29.5 في المئة من إجمالي المنح، تلتها اليمن بمبلغ 1.02 مليار درهم إماراتي (277.12 مليون دولار أمريكي) ما يمثل نسبة 11.5 في المئة من إجمالي المنح.
    </p>
    """,
    unsafe_allow_html=True
)



# البيانات
data = {
    "Fund Type": ["Grant", "Loan"],
    "2022": [1777.29, 1671.83],
    "2023": [2557.48, 620.75],
    "2024": [2414.53, 651.86]
}

df = pd.DataFrame(data)

# اختيار السنة
#year = st.selectbox("اختر السنة:", ["2022", "2023", "2024"])

# تقسيم الأعمدة (الأوسط أوسع شوية)
col1, col2, col3 = st.columns([1,2,1])

with col2:  # 👈 هنا نحط الـ selectbox
    year = st.selectbox("اختر السنة:", ["2022", "2023", "2024"])


# تجهيز البيانات للجراف
df_plot = df[["Fund Type", year]].rename(columns={year: "Spending"})

# عمل الجراف
fig = px.bar(df_plot, x="Fund Type", y="Spending", 
             color="Fund Type",
             text="Spending",
             title=f"الإنفاق عبر نوع الدعم {year}")



fig.update_traces(textposition="outside")
fig.update_layout(width=600, height=500)  # 👈 عرض أقل

# نخلي الرسم في منتصف الصفحة
col1, col2, col3 = st.columns([1,2,1])  # العمود الأوسط أوسع
with col2:
    st.plotly_chart(fig, use_container_width=False)



#st.subheader(    "شملت المساعدات الخارجية لدولة الإمارات مجموعة واسعة من المشاريع التنموية والإنسانية والخيرية. ولتحديد القطاعات التي تم توجيه المساعدات إليها بدقة، اعتٌمِد تصنيف يرتكز على 'الغرض من النشاط، وفقًا لإطار عمل وتقارير المساعدات الخارجية لدولة الإمارات وسياساتها. ويهدف هذا النهج إلى ضمان الاتساق مع المعايير الدولية وتوضيح الأثر المرجو من المساعدات.")


st.markdown(
    """
    <p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
    شملت المساعدات الخارجية لدولة الإمارات مجموعة واسعة من المشاريع التنموية والإنسانية والخيرية. ولتحديد القطاعات التي تم توجيه المساعدات إليها بدقة، اعتٌمِد تصنيف يرتكز على 'الغرض من النشاط، وفقًا لإطار عمل وتقارير المساعدات الخارجية لدولة الإمارات وسياساتها. ويهدف هذا النهج إلى ضمان الاتساق مع المعايير الدولية وتوضيح الأثر المرجو من المساعدات.
    </p>
    """,
    unsafe_allow_html=True
)

# البيانات
data = {
    "Sector": [
        "Commodity Aid",
        "Health",
        "General Programme Assistance",
        "Transport and Storage",
        "Social Services",
        "Other"
    ],
    "Spending in 2022": [276.36, 403.54, 1858.45, 97.82, 384.89, 428.06],
    "Spending in 2023": [635.76, 488.19, 998.13, 149.29, 355.54, 551.33],
    "Spending in 2024": [601.06, 510.06, 1063.07, 183.34, 243.18, 465.67],
}

df = pd.DataFrame(data)

# تحويل البيانات إلى long format عشان نرسم
df_long = df.melt(id_vars="Sector", 
                  var_name="Year", 
                  value_name="Spending")

# تنظيف اسم العمود (يبقى 2022 مش "Spending in 2022")
df_long["Year"] = df_long["Year"].str.replace("Spending in ", "")

# رسم Stacked Bar Chart
fig = px.bar(
    df_long,
    x="Year",
    y="Spending",
    color="Sector",
    text="Spending",
    title="📊 الإنفاق عبر القطاع (2022-2024)",
    barmode="stack",
    height=600,
)

# تحسينات شكل
fig.update_traces(texttemplate="%{text:.0f}", textposition="inside")
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Spending (Million AED)",
    legend_title="Sector",
    width=600, height=800
)

# عرض على Streamlit
# st.plotly_chart(fig, use_container_width=True)




# fig.update_traces(textposition="outside")


# نخلي الرسم في منتصف الصفحة
col1, col2, col3 = st.columns([1,2,1])  # العمود الأوسط أوسع
with col2:
    st.plotly_chart(fig, use_container_width=False)











