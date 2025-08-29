import streamlit as st
import pandas as pd
import plotly.express as px

# قراءة البيانات من النص مباشرة (ممكن تستبدلها بملف CSV)
data = """
Country,Aid (AED),Aid (USD),Percentage
Palestine,2454694547,668307799,58.1
Chad,661153387,180003645,15.7
Sudan,295271319,80389687,7
Jordan,248662619,67700141,5.9
Lebanon,153959229,41916479,3.6
Syria,62126439,16914359,1.5
South Sudan,57432496,15636400,1.4
Ukraine,32424159,8827705,0.8
Somalia,28837542,7851223,0.7
Congo Democracy,21246905,5784619,0.5
Yemen,18534328,5046101,0.4
Brazil,18451409,5023525,0.4
Kenya,16914650,4605132,0.4
Nigeria,13970318,3803517,0.3
Uganda,11926452,3247060,0.3
Iraq,9578721,2607874,0.2
Philippines,7521625,2047815,0.2
South Africa,7197680,1959619,0.2
Niger,6464480,1760000,0.2
Indonesia,3827083,1041950,0.1
Nepal,3674000,1000272,0.1
Cameroon,3157380,859619,0.1
Ivory Coast,3157380,859619,0.1
Ethiopia,3125172,850850,0.1
Guinea,2718957,740255,0.1
Afghanistan,2257790,614699,0.1
Burkina Faso Faso,2220329,604500,0.1
Zambia,2084721,567580,0
Thailand,1836500,500000,0
Egypt,1821883,496020,0
Kyrgyzstan,1111665,302659,0
Saint Vincent and the Grenadines,1101900,300000,0
Grenada,1101900,300000,0
Bangladesh,967300,263354,0
Pakistan,933734,254216,0
"""

# تحويل البيانات ل DataFrame
df = pd.read_csv(pd.compat.StringIO(data))

# رسم الخريطة
fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Aid (USD)",
    hover_name="Country",
    hover_data={
        "Aid (AED)": True,
        "Aid (USD)": True,
        "Percentage": True,
        "Country": False
    },
    color_continuous_scale="Blues",
    projection="natural earth",
    title="UAE Humanitarian Aid by Country (2024)"
)

# عرض الخريطة في Streamlit
st.title("UAE Humanitarian Aid Distribution (2024)")
st.plotly_chart(fig, use_container_width=True)
