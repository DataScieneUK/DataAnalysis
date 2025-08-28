import streamlit as st
# CSS لتحريك الـ sidebar لليمين


# عنوان كبير
st.title("بيانات عامة")

# نص عادي
st.write(
    "شهد عام 2024 استمرار تركز جهود المساعدات الإماراتية نحو التخفيف من حدة التداعيات للأزمات الإنسانية العالمية خاصة في المحيط الإقليمي، ويأتي في مقدمتها الأزمة الإنسانية في قطاع غزة"
)

# إدراج صورة
st.image("images/image1.png",  use_container_width=True)

st.markdown(
    """
    <style>
        /* نحرك الـ sidebar لليمين */
        [data-testid="stSidebar"] {
            float: right;
        }

        /* نخلي المحتوى الرئيسي على الشمال */
        [data-testid="stAppViewContainer"] {
            margin-right: 300px; /* عرض الـ sidebar */
            margin-left: 0;
        }

        /* نتأكد إن الـ sidebar ثابت */
        [data-testid="stSidebar"] section {
            position: fixed;
            right: 0;
            top: 0;
            height: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

