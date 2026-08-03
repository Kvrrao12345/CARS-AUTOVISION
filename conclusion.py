import streamlit as st
import pandas as pd
from pathlib import Path


st.set_page_config(
    page_title="Conclusion",
    layout="wide"
)


@st.cache_data
def load_data():
    return pd.read_csv("cars_clean.xls")

df = load_data()


st.title("Conclusion")
st.markdown("### Final Summary of the Used Car Analytics Dashboard")

st.markdown("---")


st.header("Key Findings")

st.markdown(f"""
- Total Cars Analysed : **{len(df):,}**
- Brands Available : **{df['Company_Name'].nunique()}**
- Locations Covered : **{df['Location'].nunique()}**
- Average Selling Price : **₹ {df['Price'].mean():,.0f}**
- Average Mileage : **{df['Mileage_Value'].mean():.2f}**
- Average Engine Capacity : **{df['Engine_Value'].mean():.0f} cc**
- Average Power : **{df['Power_Value'].mean():.0f} bhp**
""")

st.markdown("---")


st.header("Business Recommendations")

st.success("""
✔ Focus on brands with consistently high resale values.

✔ Maintain balanced inventory across fuel types.

✔ Prioritize vehicles with lower kilometers driven.

✔ Monitor regional demand before pricing vehicles.

✔ Use market trends to optimize inventory planning.

✔ Promote vehicles with better mileage and newer models.
""")




st.header("Future Enhancements")

st.markdown("""
- Add Machine Learning based price prediction.
- Build recommendation system for buyers.
- Enable user-uploaded datasets.
- Add advanced dashboard filters.
- Create downloadable PDF reports.
- Integrate live automobile market data.
- Deploy on Streamlit Community Cloud.
""")

st.markdown("---")


st.header("Final Conclusion")

st.info("""
The AutoVision dashboard demonstrates how raw automotive data can be converted
into actionable business intelligence using modern data analytics techniques.
The combination of Python, Pandas, Plotly, and Streamlit enables users to
explore market trends, compare vehicle characteristics, and gain valuable
insights through an intuitive and interactive interface.

This project highlights practical skills in data preprocessing, exploratory
data analysis, visualization, and dashboard development, making it an excellent
portfolio project for aspiring Data Analysts and Data Scientists.
""")

st.markdown("---")

st.caption("© 2026 | AutoVision - Used Car Analytics Dashboard | Developed by K. Vivek Rao")