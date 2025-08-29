import streamlit as st

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


st.title("إحصائيات أخري")



st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
تُصنَّف دول العالم إلى خمس فئات رئيسية وفقًا لمستوى الدخل، وذلك استناداً إلى تصنيفات من مؤسسات دولية معتمدة، كالبنك الدولي وكذلك القائمة الاسترشادية للجنة المساعدات الإنمائية التابعة لمنظمة التعاون الاقتصادي والتنمية، وعلى أساس نصيب الفرد من الدخل القومي الإجمالي (GNI) وتشمل الفئات:   الشريحة الدنيا من متوسط الدخل، والشريحة العليا من متوسط الدخل، والدخل العالي، والدخل المنخفض، والدول الأقل نمواً.

    </p>""",unsafe_allow_html=True)


st.image("images/image7.png", use_container_width =False, width=600)




st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
خصصت دولة الإمارات من مساعداتها الخارجية، في عام 2024، ما قيمته 4.22 مليار درهم (1.15 مليار دولار أمريكي) للمساعدات الإنسانية، وهو ما يمثل نسبة 37.48 في المئة من إجمالي مساعداتها خلال العام. وقد استفادت 53 دولة حول العالم من تلك المساعدات  بما في ذلك 17 دولة من الدول الأقل نمواً بإجمالي 1.12 مليار درهم إماراتي (304.60 مليون دولار أمريكي) وتمثل المساعدات الإنسانية للدول الأقل نمواً نسبة 26.5 في المئة من إجمالي المساعدات الإنسانية التي قدمتها دولة الإمارات خلال العام وبزيادة قدرها 10 في المئة مقارنة بعام 2023 حيث كانت 1 مليار درهم إماراتي (277.4 مليون دولار أمريكي)
    </p>""",unsafe_allow_html=True)


st.image("images/image8.png", use_container_width =False, width=600)



st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
وقد تركزت المساعدات في شريحة الدول الأقل نموا بصفة رئيسية في كل من تشاد والسودان  بنسب  59 في المئة و26 في المئة من إجمالي تلك المساعدات على التوالي.

    </p>""",unsafe_allow_html=True)


st.image("images/image9.png", use_container_width =False, width=600)

