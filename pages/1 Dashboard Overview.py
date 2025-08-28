import streamlit as st
# CSS لتحريك الـ sidebar لليمين
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            right: 0;
            left: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# عنوان كبير
st.title("بيانات عامة")

# نص عادي
st.write(
    "شهد عام 2024 استمرار تركز جهود المساعدات الإماراتية نحو التخفيف من حدة التداعيات للأزمات الإنسانية العالمية خاصة في المحيط الإقليمي، ويأتي في مقدمتها الأزمة الإنسانية في قطاع غزة"
)

# إدراج صورة
st.image("images/image1.png",  use_container_width=True)


