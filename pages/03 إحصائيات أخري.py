import streamlit as st
import pandas as pd
import plotly.express as px

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



# st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
#                 تُصنَّف دول العالم إلى خمس فئات رئيسية وفقًا لمستوى الدخل، وذلك استناداً إلى تصنيفات من مؤسسات دولية معتمدة، كالبنك الدولي وكذلك القائمة الاسترشادية للجنة المساعدات الإنمائية التابعة لمنظمة التعاون الاقتصادي والتنمية، وعلى أساس نصيب الفرد من الدخل القومي الإجمالي (GNI) وتشمل الفئات:   الشريحة الدنيا من متوسط الدخل، والشريحة العليا من متوسط الدخل، والدخل العالي، والدخل المنخفض، والدول الأقل نمواً.
#                 </p>
#                 """,unsafe_allow_html=True)


# st.image("images/image7.png", use_container_width =False, width=750)




st.set_page_config(layout="wide")

# --- البيانات ---
data = {
    "Income Level": [
        "Least Developed Countries",
        "Lower Middle Income",
        "Low Income",
        "High Income",
        "Upper Middle Income",
        "Multi-country"
    ],
    "Spending in 2022": [914.08, 420.9, 32.04, 150.24, 1622.75, 309.13],
    "Spending in 2023": [715.73, 878.19, 281.34, 467.11, 561.76, 274.1],
    "Spending in 2024": [1349.59, 357.04, 17.53, 95.3, 974.99, 271.94],
}

df = pd.DataFrame(data)

# --- تحويل البيانات إلى long format ---
df_long = df.melt(id_vars="Income Level", var_name="Year", value_name="Spending")
df_long["Year"] = df_long["Year"].str.replace("Spending in ", "")

# --- تقسيم الأعمدة ---
col1, col2, col3 = st.columns([1,3,1])

# اختيار السنة
with col1:
    selected_year = st.radio(
        "اختر السنة:",
        options=["2022", "2023", "2024"],
        index=2,
        key="income_year_selector"
    )

# تصفية البيانات على السنة المختارة
df_selected = df_long[df_long["Year"] == selected_year].copy()

# حساب النسبة المؤوية
total_spending = df_selected["Spending"].sum()
df_selected["Percentage"] = (df_selected["Spending"] / total_spending) * 100

# عمود يجمع الرقم + النسبة للعرض على الأعمدة
df_selected["Label"] = df_selected.apply(
    lambda row: f"{row['Spending']:.0f} ({row['Percentage']:.1f}%)", axis=1
)

# --- رسم الجراف ---
fig = px.bar(
    df_selected,
    x="Income Level",
    y="Spending",
    color="Income Level",
    text="Label",
    title=f"📊 الإنفاق حسب مستوى الدخل - {selected_year}",
    height=600
)

fig.update_traces(textposition="outside")
fig.update_layout(
    xaxis_title="Income Level",
    yaxis_title="Spending (Million AED)",
    showlegend=False,  # كل عمود يمثل فئة
    width=900,
    title_x=0.5
)

# عرض الجراف في العمود الأوسط
with col2:
    st.plotly_chart(fig, use_container_width=False)


# st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
# خصصت دولة الإمارات من مساعداتها الخارجية، في عام 2024، ما قيمته 4.22 مليار درهم (1.15 مليار دولار أمريكي) للمساعدات الإنسانية، وهو ما يمثل نسبة 37.48 في المئة من إجمالي مساعداتها خلال العام. وقد استفادت 53 دولة حول العالم من تلك المساعدات  بما في ذلك 17 دولة من الدول الأقل نمواً بإجمالي 1.12 مليار درهم إماراتي (304.60 مليون دولار أمريكي) وتمثل المساعدات الإنسانية للدول الأقل نمواً نسبة 26.5 في المئة من إجمالي المساعدات الإنسانية التي قدمتها دولة الإمارات خلال العام وبزيادة قدرها 10 في المئة مقارنة بعام 2023 حيث كانت 1 مليار درهم إماراتي (277.4 مليون دولار أمريكي)
#     </p>
#     """,unsafe_allow_html=True)


# st.image("images/image8.png", use_container_width =False, width=600)
################################################################################
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# --- البيانات ---
data = {
    "Income Level": ["AED", "USD"],
    "2022": [1.6, 0.43],
    "2023": [4.9, 1.33],
    "2024": [4.22, 1.14],
}

df = pd.DataFrame(data)

# --- اختيار السنة ---
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    selected_year = st.radio(
        "اختر السنة:",
        ["2022", "2023", "2024"],
        index=2,
        key="horizontal_bar_selector"
    )

# تجهيز البيانات
df_selected = df[["Income Level", selected_year]].rename(columns={selected_year: "Value"})
total = df_selected["Value"].sum()
# df_selected["Percentage"] = (df_selected["Value"] / total) * 100

# --- رسم Bar Chart أفقي ---
fig = px.bar(
    df_selected,
    x="Value",
    y="Income Level",
    orientation="h",
    text=df_selected.apply(lambda row: f"{row['Value']}", axis=1),
    color="Income Level",
    title=f"📊 المساعدات الإنسانية, بالمليار {selected_year}"
)

fig.update_traces(
    textposition="outside"
)

fig.update_layout(
    xaxis_title="القيمة",
    yaxis_title="",
    width=700,
    height=400,
    title_x=0.5
)

with col2:
    st.plotly_chart(fig, use_container_width=False)


##############################################################

# st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
#     وقد تركزت المساعدات في شريحة الدول الأقل نموا بصفة رئيسية في كل من تشاد والسودان  بنسب  59 في المئة و26 في المئة من إجمالي تلك المساعدات على التوالي.
#     </p>
#     """,unsafe_allow_html=True)


# st.image("images/image9.png", use_container_width =False, width=600)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# --- البيانات ---
data = {
    "Country": ["Chad", "Sudan", "Other"],
    "2022": [0.82, 13.76, 199.65],
    "2023": [102.19, 25.8, 60.27],
    "2024": [180, 80.39, 44.2],
}

df = pd.DataFrame(data)

# اختيار السنة من القائمة (radio)
col1, col2 = st.columns([1, 4])
with col1:
    selected_year = st.radio("اختر السنة:", ["2022", "2023", "2024"], index=2, key="year_selector_countries")

# تجهيز البيانات للسنة المختارة
df_plot = df[["Country", selected_year]].rename(columns={selected_year: "Spending"})

# --- رسم الجراف ---
fig = px.bar(
    df_plot,
    x="Country",
    y="Spending",
    color="Country",
    text="Spending",
    title=f"📊 الإنفاق حسب الدولة في {selected_year}"
)

fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
fig.update_layout(
    xaxis_title="الدولة",
    yaxis_title="الإنفاق (مليون)",
    width=700,
    height=500,
    title_x=0.5
)

# عرض الرسم في منتصف الصفحة
col_left, col_center, col_right = st.columns([1, 3, 1])
with col_center:
    st.plotly_chart(fig, use_container_width=False)
############################################################

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# --- البيانات (النسب المئوية) ---
data = {
    "Country": ["Chad", "Sudan", "Other"],
    "2022": [0.41, 6.89, 92.7],
    "2023": [54.28, 13.70, 32.02],
    "2024": [59.09, 26.39, 14.51],
}

df = pd.DataFrame(data)

# اختيار السنة
col1, col2 = st.columns([1, 4])
with col1:
    selected_year = st.radio("اختر السنة:", ["2022", "2023", "2024"], index=2, key="year_selector_percentages")

# تجهيز البيانات للسنة المختارة
df_plot = df[["Country", selected_year]].rename(columns={selected_year: "Percentage"})

# --- رسم الجراف ---
fig = px.bar(
    df_plot,
    x="Country",
    y="Percentage",
    color="Country",
    text="Percentage",
    title=f"📊 نسبة الإنفاق حسب الدولة في {selected_year}"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)
fig.update_layout(
    xaxis_title="الدولة",
    yaxis_title="النسبة المئوية %",
    width=700,
    height=500,
    title_x=0.5,
    yaxis=dict(range=[0, 100])  # عشان تبقى النسب كلها واضحة على نفس المقياس
)

# عرض الرسم في المنتصف
col_left, col_center, col_right = st.columns([1, 3, 1])
with col_center:
    st.plotly_chart(fig, use_container_width=False)



######################################################################################

# st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
# حيث تشكل المساعدات السلعية نسبة 51.4 في المئة من إجمالي قيمة المساعدات الإنسانية .  وتشكل المساعدات في قطاع الصحة نسبة 23.4 في المئة من المساعدات الإنسانية  ويليها مساعدات دعم البرامج العامة بنسبة 22.8 في المئة،  و باقي البرامج 2.4 %
#     </p>
#     """,unsafe_allow_html=True)


# st.image("images/image10.png", use_container_width =False, width=600)

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# --- البيانات ---
data = {
    "Sector": ["Commodity Aid", "Health", "General Programme Assistance", "Other"],
    "2022": [234.9, 88.71, 107.49, 4.77],
    "2023": [577.87, 404.64, 310.49, 41.84],
    "2024": [590.8, 269.43, 262.53, 26.53],
}

df = pd.DataFrame(data)

# --- اختيار السنة على اليسار والـ Pie Chart على اليمين ---
col1, col2 = st.columns([1, 4])
with col1:
    selected_year = st.radio(
        "اختر السنة:",
        ["2022", "2023", "2024"],
        index=2,
        key="year_selector_pie"
    )

# تجهيز البيانات
df_plot = df[["Sector", selected_year]].rename(columns={selected_year: "Spending"})

# حساب النسبة المئوية
df_plot["Percentage"] = (df_plot["Spending"] / df_plot["Spending"].sum()) * 100

# النص داخل القطاعات
df_plot["Label"] = df_plot.apply(lambda row: f"{row['Spending']:.2f} ({row['Percentage']:.1f}%)", axis=1)

# --- رسم الـ Pie chart ---
fig = px.pie(
    df_plot,
    names="Sector",
    values="Spending",
    hole=0.4,
    title=f"📊 توزيع الإنفاق على القطاعات في {selected_year}"
)

fig.update_traces(
    text=df_plot["Label"],
    textinfo="text",  # نظهر النصوص المخصصة فقط
    textposition="inside",
    hovertemplate="<b>%{label}</b><br>الإنفاق: %{value:.2f}<br>النسبة: %{percent}"
)

fig.update_layout(
    width=700,
    height=500,
    title_x=0.5
)


col_left, col_center, col_right = st.columns([1, 3, 1])
with col_center:
    st.plotly_chart(fig, use_container_width=False)

# # عرض الرسم في العمود الكبير
# with col2:
#     st.plotly_chart(fig, use_container_width=False)

######################################################################################

# st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
# 	ظلّت مصادر التمويل الحكومية خلال عام 2024، المصدر الرئيسي للمساعدات، والتي تشمل مساهمات الحكومة والقطاع العام، حيث ساهمت بقيمةـ 9.72 مليار درهم (2.65 مليار دولار أمريكي)، أي ما نسبته 86.27 في المئة من إجمالي المساعدات. 
# وقد ساهمت مصادر تمويل القطاع الخاص، والتي تشمل الأفراد والقطاع الخاص، بمبلغ 1.55 مليار درهم إماراتي (421.0 مليون دولار أمريكي)، أي بنسبة 13.73 في المئة. من إجمالي المساعدات الخارجية لدولة الإمارات. وتعكس الجهود المشتركة لكلا القطاعين العام والخاص نموذج تمويلي قوي ومتنوع يعزز من مكانة دولة الإمارات كجهة مانحة رائدة على الساحة العالمية في مجال المساعدات الخارجية.
# 	</p>
# 	""",unsafe_allow_html=True)


# st.image("images/image11.png", use_container_width =False, width=600)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# --- البيانات ---
data = {
    "Source_of_Funds": ["Official", "Private"],
    "2022": [2958.42, 490.7],
    "2023": [2785.99, 392.24],
    "2024": [2645.39, 421.0],
}

df = pd.DataFrame(data)

# --- اختيار السنة على اليسار والـ Pie Chart على اليمين ---
col1, col2 = st.columns([1, 4])
with col1:
    selected_year = st.radio(
        "اختر السنة:",
        ["2022", "2023", "2024"],
        index=2,
        key="year_selector_funds"
    )

# تجهيز البيانات
df_plot = df[["Source_of_Funds", selected_year]].rename(columns={selected_year: "Spending"})

# حساب النسبة المئوية
df_plot["Percentage"] = (df_plot["Spending"] / df_plot["Spending"].sum()) * 100

# النص داخل القطاعات
df_plot["Label"] = df_plot.apply(lambda row: f"{row['Spending']:.2f} ({row['Percentage']:.1f}%)", axis=1)

# --- رسم الـ Pie chart ---
fig = px.pie(
    df_plot,
    names="Source_of_Funds",
    values="Spending",
    hole=0.4,
    title=f"📊 توزيع مصادر التمويل في {selected_year}"
)

fig.update_traces(
    text=df_plot["Label"],
    textinfo="text",
    textposition="inside",
    hovertemplate="<b>%{label}</b><br>الإنفاق: %{value:.2f}<br>النسبة: %{percent}"
)

fig.update_layout(
    width=700,
    height=500,
    title_x=0.5
)

# # عرض الرسم في العمود الكبير
# with col2:
#     st.plotly_chart(fig, use_container_width=False)

# عرض الرسم في المنتصف
col_left, col_center, col_right = st.columns([1, 3, 1])
with col_center:
    st.plotly_chart(fig, use_container_width=False)

######################################################################################

st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
تنوعت أساليب تنفيذ المساعدات الخارجية من قبل الجهات والمؤسسات المانحة في دولة الإمارات بما يعكس حرصها على تبني نهج متنوع يتماشى مع طبيعة المشاريع التنموية والإنسانية والخيرية. وخلال عام 2024، تم تنفيذ المساعدات الخارجية الإماراتية عبر أربع قنوات رئيسية:
المساعدات التي تمت عن طريق المشاريع المنفذة بشكل مباشر: بنسبة 38.3 في المئة
المساعدات ثنائيةالأطراف إلى الحكومات: وتمثل نسبة 33.8 في المئة 
المساعدات المخصصة الغرض إلى المنظمات متعددة الأطراف: وشكلت نسبة 11.2 في المئة 
المساعدات إلى المنظمات المحلية غير الحكومية ومؤسسات المجتمع المدني: وتمثل نسبة 10.8 في المئة 
تشكل هذه القنوات الأربع مجتمعة نسبة 94.2 في المئة من إجمالي المساعدات الخارجية لدولة الإمارات في عام 2024. أما النسبة المتبقية فقد تم توزيعها من خلال قنوات إضافية مثل المساعدات إلى المنظمات الدولية غير الحكومية ومساعدات التعاون الفني والخبراء والمنح الدراسية.
	</p>
	""",unsafe_allow_html=True)


st.image("images/image12.png", use_container_width =False, width=800)


######################################################################################


st.markdown("""<p style='color:#5d6063; font-size:20px; font-weight:bold; text-align:justify;'>
	و هنا توزيع لكامل مصادر الدعم, عبر المؤسسات المختلفة
	</p>
	""",unsafe_allow_html=True)


st.image("images/image13.png", use_container_width =False, width=800)


######################################################################################















