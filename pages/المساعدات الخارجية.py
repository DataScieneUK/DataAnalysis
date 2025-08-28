import streamlit as st
# CSS لتحريك الـ sidebar لليمين


# عنوان كبير
st.title("بيانات عامة")


st.subheader(f"شهد عام 2024 استمرار تركز جهود المساعدات الإماراتية نحو التخفيف من حدة التداعيات للأزمات الإنسانية العالمية خاصة في المحيط الإقليمي، ويأتي في مقدمتها الأزمة الإنسانية في قطاع غزة")

st.image("images/image1.png",  use_container_width=True)



st.subheader(f"تتعلق المساعدات الإنسانية، بالجهود المبذولة لإنقاذ الأرواح، بما في ذلك عمليات الطوارئ والإغاثة حيث خصصت دولة الإمارات نسبة 37.48 في المئة للمساعدات الإنسانية، بقيمة 4.22 مليار درهم (1.15مليار دولار أمريكي). أما المساعدات التنموية،  58.2 في المئة ، بقيمة 6.56 مليار درهم (1.79 مليار دولار أمريكي)، .  بينما المساعدات الخيرية بمبلغ 483.20 مليون درهم (131.55 مليون دولار أمريكي)، بنسبة 4.29 في المئة ")

st.image("images/image2.png",  use_container_width=True)




st.subheader(f"بلغ إجمالي المساعدات الخارجية لدولة الإمارات، في عام 2024، ما قيمته 11.26 مليار درهم (3.07 مليار دولار أمريكي)، في حين وصلت قيمة المساعدات الإنمائية الرسمية إلى مبلغ 8.97 مليار درهم (2.44 مليار دولار أمريكي)")
st.image("images/Image3.png",  use_container_width=True)


#st.subheader(f"")
#st.image("images/image.png",  use_container_width=True)



#st.subheader(f"")
#st.image("images/image.png",  use_container_width=True)



#st.subheader(f"")
#st.image("images/image.png",  use_container_width=True)



#st.subheader(f"")
#st.image("images/image.png",  use_container_width=True)



#st.subheader(f"")
#st.image("images/image.png",  use_container_width=True)



#st.subheader(f"")
#st.image("images/image.png",  use_container_width=True)



#st.subheader(f"")
#st.image("images/image.png",  use_container_width=True)



#st.subheader(f"")
#st.image("images/image.png",  use_container_width=True)










st.set_page_config(
    layout="wide",
    page_title="UAE Foreign Aid Hub",
    page_icon="🇦🇪",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Right-to-Left (RTL) and text alignment ---
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






