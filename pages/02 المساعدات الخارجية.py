import streamlit as st

# --- Page Config ---
st.set_page_config(
    layout="wide",
    page_title="UAE Foreign Aid Hub",
    page_icon="🇦🇪",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for RTL, colors, and centered images ---
st.markdown("""
<style>
    /* RTL for the whole app */
    div.stApp {
        direction: rtl;
        text-align: right;
        background-color: #f0f2f6; /* Light background */
    }

    /* Titles colors */
    h1 {
        color: #004d40; /* Dark teal */
        text-align: right;
    }
    h2, h3 {
        color: #00695c;
        text-align: right;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #e0e0e0;
        direction: rtl;
        text-align: right;
    }

    /* Centered images with fixed width */
    .centered-img {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    .centered-img img {
        width: 400px;
        border-radius: 10px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #00897b;
        color: white;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #00796b;
    }
</style>
""", unsafe_allow_html=True)

# --- Content ---

# عنوان كبير
st.title("المساعدات الخارجية")

st.subheader(
    "في عام 2024، ركزت المساعدات الخارجية لدولة الإمارات على خمسة أهداف رئيسية من أهداف التنمية المستدامة، "
    "شكلت مجتمعة أكثر من 84 في المئة من إجمالي المساعدات الموجهة لدعم القضايا العالمية الملحّة."
)

st.markdown(
    '<div class="centered-img"><img src="images/image4.png"></div>',
    unsafe_allow_html=True
)

st.subheader(
    "شكلت المنح النسبة الأكبر من تقديم المساعدات الخارجية الإماراتية في عام 2024، بنسبة 78.7 في المئة من الإجمالي، "
    "مبلغ 8.87 مليار درهم إماراتي (2.4 مليار دولار أمريكي). وقد استفادت من هذه المنح 133 دولة، من بينها 38 دولة "
    "مصنفة ضمن أقل البلدان نمواً. حيث حصلت فلسطين على الحصة الأكبر بقيمة 2.62 مليار درهم إماراتي (712.89 مليون "
    "دولار أمريكي)، ما يمثل نسبة 29.5 في المئة من إجمالي المنح، تلتها اليمن بمبلغ 1.02 مليار درهم إماراتي "
    "(277.12 مليون دولار أمريكي) ما يمثل نسبة 11.5 في المئة من إجمالي المنح."
)
st.markdown(
    '<div class="centered-img"><img src="images/image5.png"></div>',
    unsafe_allow_html=True
)

st.subheader(
    "شملت المساعدات الخارجية لدولة الإمارات مجموعة واسعة من المشاريع التنموية والإنسانية والخيرية. "
    "ولتحديد القطاعات التي تم توجيه المساعدات إليها بدقة، اعتُمد تصنيف يرتكز على 'الغرض من النشاط، وفقًا لإطار عمل "
    "وتقارير المساعدات الخارجية لدولة الإمارات وسياساتها. ويهدف هذا النهج إلى ضمان الاتساق مع المعايير الدولية "
    "وتوضيح الأثر المرجو من المساعدات."
)
st.markdown(
    '<div class="centered-img"><img src="images/image6.png"></div>',
    unsafe_allow_html=True
)











