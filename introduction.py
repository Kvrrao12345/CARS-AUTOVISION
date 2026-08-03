import streamlit as st
import pandas as pd
from pathlib import Path



st.set_page_config(
    page_title="Introduction",
    layout="wide"
)


@st.cache_data
def load_data():
    return pd.read_csv("cars_clean.xls")

df = load_data()


st.title("AutoVision")
st.subheader("Used Car Analytics Dashboard")

st.markdown("---")


st.header("Business Problem")

st.write("""
The used car market consists of thousands of vehicles with varying prices,
brands, fuel types, and specifications. Buyers often struggle to determine
whether a listed vehicle is fairly priced, while sellers need to understand
current market trends to maximize their returns.

This dashboard transforms raw vehicle data into meaningful business insights,
helping users understand pricing patterns, brand performance, customer
preferences, and overall market trends through interactive visualizations.
""")


st.header("Project Objectives")

st.markdown("""
- Analyze the used car market.
- Study vehicle price distribution.
- Compare leading automobile brands.
- Understand fuel and transmission preferences.
- Explore relationships between price, mileage, engine size, and power.
- Generate actionable business insights.
""")

st.markdown("---")


st.header("Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Total Records:** {len(df):,}")
    st.write(f"**Total Features:** {df.shape[1]}")
    st.write(f"**Brands:** {df['Company_Name'].nunique()}")
    st.write(f"**Locations:** {df['Location'].nunique()}")

with col2:
    st.write(f"**Fuel Types:** {df['Fuel_Type'].nunique()}")
    st.write(f"**Transmission Types:** {df['Transmission'].nunique()}")
    st.write(f"**Average Price:** ₹ {df['Price'].mean():,.0f}")
    st.write(f"**Average Mileage:** {df['Mileage_Value'].mean():.2f}")

st.markdown("---")


st.header("Key Performance Indicators")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Total Cars",
        f"{len(df):,}"
    )

with c2:
    st.metric(
        "Brands",
        df["Company_Name"].nunique()
    )

with c3:
    st.metric(
        "Locations",
        df["Location"].nunique()
    )

with c4:
    st.metric(
        "Avg Price",
        f"₹ {df['Price'].mean():,.0f}"
    )

st.markdown("---")


st.header("Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.markdown("---")


st.header("Why This Dashboard?")

st.info("""
This dashboard is designed to help analysts, buyers, sellers, and automobile
enthusiasts understand the used car market using interactive visualizations
and business intelligence techniques.

It demonstrates practical skills in:

✔ Data Cleaning

✔ Exploratory Data Analysis (EDA)

✔ Business Intelligence

✔ Interactive Dashboard Development

✔ Data Visualization using Plotly

✔ Streamlit Application Development
""")

st.markdown("---")

st.success("Use the sidebar to navigate to the Exploratory Data Analysis page.")