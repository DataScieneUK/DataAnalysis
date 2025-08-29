import streamlit as st

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
st.title("بيانات عامة")


#st.subheader(f"شهد عام 2024 استمرار تركز جهود المساعدات الإماراتية نحو التخفيف من حدة التداعيات للأزمات الإنسانية العالمية خاصة في المحيط الإقليمي، ويأتي في مقدمتها الأزمة الإنسانية في قطاع غزة")

st.markdown(
    """
    <p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
 شهد عام 2024 استمرار تركز جهود المساعدات الإماراتية نحو التخفيف من حدة التداعيات للأزمات الإنسانية العالمية خاصة في المحيط الإقليمي، ويأتي في مقدمتها الأزمة الإنسانية في قطاع غزة
    </p>
    """,
    unsafe_allow_html=True
)


st.image("images/image1.png", use_container_width =False, width=600)



#st.subheader(f"تتعلق المساعدات الإنسانية، بالجهود المبذولة لإنقاذ الأرواح، بما في ذلك عمليات الطوارئ والإغاثة حيث خصصت دولة الإمارات نسبة 37.48 في المئة للمساعدات الإنسانية، بقيمة 4.22 مليار درهم (1.15مليار دولار أمريكي). أما المساعدات التنموية،  58.2 في المئة ، بقيمة 6.56 مليار درهم (1.79 مليار دولار أمريكي)، .  بينما المساعدات الخيرية بمبلغ 483.20 مليون درهم (131.55 مليون دولار أمريكي)، بنسبة 4.29 في المئة ")

st.markdown(
    """
    <p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
 تتعلق المساعدات الإنسانية، بالجهود المبذولة لإنقاذ الأرواح، بما في ذلك عمليات الطوارئ والإغاثة حيث خصصت دولة الإمارات نسبة 37.48 في المئة للمساعدات الإنسانية، بقيمة 4.22 مليار درهم (1.15مليار دولار أمريكي). أما المساعدات التنموية،  58.2 في المئة ، بقيمة 6.56 مليار درهم (1.79 مليار دولار أمريكي)، .  بينما المساعدات الخيرية بمبلغ 483.20 مليون درهم (131.55 مليون دولار أمريكي)، بنسبة 4.29 في المئة 
    </p>
    """,
    unsafe_allow_html=True
)

st.image("images/image2.png", use_container_width =False, width=600)




#st.subheader(f"بلغ إجمالي المساعدات الخارجية لدولة الإمارات، في عام 2024، ما قيمته 11.26 مليار درهم (3.07 مليار دولار أمريكي)، في حين وصلت قيمة المساعدات الإنمائية الرسمية إلى مبلغ 8.97 مليار درهم (2.44 مليار دولار أمريكي)")


st.markdown(
    """
    <p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
 بلغ إجمالي المساعدات الخارجية لدولة الإمارات، في عام 2024، ما قيمته 11.26 مليار درهم (3.07 مليار دولار أمريكي)، في حين وصلت قيمة المساعدات الإنمائية الرسمية إلى مبلغ 8.97 مليار درهم (2.44 مليار دولار أمريكي)
    </p>
    """,
    unsafe_allow_html=True
)

st.image("images/Image3.png", use_container_width =False, width=600)























