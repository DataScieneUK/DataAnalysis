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
                </p>
                """,unsafe_allow_html=True)


st.image("images/image7.png", use_container_width =False, width=750)




st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
خصصت دولة الإمارات من مساعداتها الخارجية، في عام 2024، ما قيمته 4.22 مليار درهم (1.15 مليار دولار أمريكي) للمساعدات الإنسانية، وهو ما يمثل نسبة 37.48 في المئة من إجمالي مساعداتها خلال العام. وقد استفادت 53 دولة حول العالم من تلك المساعدات  بما في ذلك 17 دولة من الدول الأقل نمواً بإجمالي 1.12 مليار درهم إماراتي (304.60 مليون دولار أمريكي) وتمثل المساعدات الإنسانية للدول الأقل نمواً نسبة 26.5 في المئة من إجمالي المساعدات الإنسانية التي قدمتها دولة الإمارات خلال العام وبزيادة قدرها 10 في المئة مقارنة بعام 2023 حيث كانت 1 مليار درهم إماراتي (277.4 مليون دولار أمريكي)
    </p>
    """,unsafe_allow_html=True)


st.image("images/image8.png", use_container_width =False, width=600)



st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
    وقد تركزت المساعدات في شريحة الدول الأقل نموا بصفة رئيسية في كل من تشاد والسودان  بنسب  59 في المئة و26 في المئة من إجمالي تلك المساعدات على التوالي.
    </p>
    """,unsafe_allow_html=True)


st.image("images/image9.png", use_container_width =False, width=600)




st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
حيث تشكل المساعدات السلعية نسبة 51.4 في المئة من إجمالي قيمة المساعدات الإنسانية .  وتشكل المساعدات في قطاع الصحة نسبة 23.4 في المئة من المساعدات الإنسانية  ويليها مساعدات دعم البرامج العامة بنسبة 22.8 في المئة،  و باقي البرامج 2.4 %
    </p>
    """,unsafe_allow_html=True)


st.image("images/image10.png", use_container_width =False, width=600)



st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
	ظلّت مصادر التمويل الحكومية خلال عام 2024، المصدر الرئيسي للمساعدات، والتي تشمل مساهمات الحكومة والقطاع العام، حيث ساهمت بقيمةـ 9.72 مليار درهم (2.65 مليار دولار أمريكي)، أي ما نسبته 86.27 في المئة من إجمالي المساعدات. 
وقد ساهمت مصادر تمويل القطاع الخاص، والتي تشمل الأفراد والقطاع الخاص، بمبلغ 1.55 مليار درهم إماراتي (421.0 مليون دولار أمريكي)، أي بنسبة 13.73 في المئة. من إجمالي المساعدات الخارجية لدولة الإمارات. وتعكس الجهود المشتركة لكلا القطاعين العام والخاص نموذج تمويلي قوي ومتنوع يعزز من مكانة دولة الإمارات كجهة مانحة رائدة على الساحة العالمية في مجال المساعدات الخارجية.

	</p>
	""",unsafe_allow_html=True)


st.image("images/image11.png", use_container_width =False, width=600)



st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
تنوعت أساليب تنفيذ المساعدات الخارجية من قبل الجهات والمؤسسات المانحة في دولة الإمارات بما يعكس حرصها على تبني نهج متنوع يتماشى مع طبيعة المشاريع التنموية والإنسانية والخيرية. وخلال عام 2024، تم تنفيذ المساعدات الخارجية الإماراتية عبر أربع قنوات رئيسية:
المساعدات التي تمت عن طريق المشاريع المنفذة بشكل مباشر: بنسبة 38.3 في المئة
المساعدات ثنائيةالأطراف إلى الحكومات: وتمثل نسبة 33.8 في المئة 
المساعدات المخصصة الغرض إلى المنظمات متعددة الأطراف: وشكلت نسبة 11.2 في المئة 
المساعدات إلى المنظمات المحلية غير الحكومية ومؤسسات المجتمع المدني: وتمثل نسبة 10.8 في المئة 
تشكل هذه القنوات الأربع مجتمعة نسبة 94.2 في المئة من إجمالي المساعدات الخارجية لدولة الإمارات في عام 2024. أما النسبة المتبقية فقد تم توزيعها من خلال قنوات إضافية مثل المساعدات إلى المنظمات الدولية غير الحكومية ومساعدات التعاون الفني والخبراء والمنح الدراسية.

	</p>
	""",unsafe_allow_html=True)


st.image("images/image12.png", use_container_width =False, width=600)





st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
	و هنا توزيع لكامل مصادر الدعم, عبر المؤسسات المختلفة
	</p>
	""",unsafe_allow_html=True)


st.image("images/image13.png", use_container_width =False, width=600)

