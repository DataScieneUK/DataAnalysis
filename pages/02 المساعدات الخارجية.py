import streamlit as st
# CSS لتحريك الـ sidebar لليمين


# عنوان كبير
st.title("المساعدات الخارجية")


st.subheader(f"في عام 2024، ركزت المساعدات الخارجية لدولة الإمارات على خمسة أهداف رئيسية من أهداف التنمية المستدامة، شكلت مجتمعة أكثر من 84 في المئة من إجمالي المساعدات الموجهة لدعم القضايا العالمية الملحّة.")

st.image("images/image4.png",  use_container_width=True, width=300)


st.subheader(f"شكلت المنح النسبة الأكبر من تقديم المساعدات الخارجية الإماراتية في عام 2024، بنسبة 78.7 في المئة من الإجمالي، مبلغ 8.87 مليار درهم إماراتي (2.4 مليار دولار أمريكي). وقد استفادت من هذه المنح 133 دولة، من بينها 38 دولة مصنفة ضمن أقل البلدان نمواً. حيث حصلت فلسطين على الحصة الأكبر بقيمة 2.62 مليار درهم إماراتي (712.89 مليون دولار أمريكي)، ما يمثل نسبة 29.5 في المئة من إجمالي المنح، تلتها اليمن بمبلغ 1.02 مليار درهم إماراتي (277.12 مليون دولار أمريكي) ما يمثل نسبة 11.5 في المئة من إجمالي المنح.")
st.image("images/image5.png",  use_container_width=True, width=300)



st.subheader(f"شملت المساعدات الخارجية لدولة الإمارات مجموعة واسعة من المشاريع التنموية والإنسانية والخيرية. ولتحديد القطاعات التي تم توجيه المساعدات إليها بدقة، اعتٌمِد تصنيف يرتكز على 'الغرض من النشاط، وفقًا لإطار عمل وتقارير المساعدات الخارجية لدولة الإمارات وسياساتها. ويهدف هذا النهج إلى ضمان الاتساق مع المعايير الدولية وتوضيح الأثر المرجو من المساعدات.")
st.image("images/image6.png",  use_container_width=True, width=300)



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











