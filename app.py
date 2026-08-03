import streamlit as st
import pandas as pd
from pathlib import Path


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AutoVision | Used Car Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.image(
"https://images.unsplash.com/photo-1503376780353-7e6692767b70",
use_container_width=True
)


@st.cache_data
def load_data():
    return pd.read_csv("cars_clean.xls")

df = load_data()


st.sidebar.title("AutoVision")

st.sidebar.markdown("---")

st.sidebar.success("Used Car Analytics Dashboard")

st.sidebar.info(
    """
Developed using:

- Python
- Streamlit
- Pandas
- Plotly
"""
)

st.sidebar.markdown("---")

st.sidebar.write("### Dataset Summary")

st.sidebar.metric("Total Cars", f"{len(df):,}")

st.sidebar.metric(
    "Brands",
    df["Company_Name"].nunique()
)

st.sidebar.metric(
    "Locations",
    df["Location"].nunique()
)

st.sidebar.markdown("---")

st.sidebar.caption("Version 1.0")


st.title("AutoVision")
st.subheader("Used Car Analytics Dashboard")

st.markdown(
"""
Welcome to **AutoVision**, an interactive dashboard developed using
**Streamlit**, **Pandas**, and **Plotly**.

Use the navigation menu on the left sidebar to explore:

- Introduction
- Exploratory Data Analysis
- Insights
- Conclusion
"""
)

st.markdown("---")


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Cars", f"{len(df):,}")

with col2:
    st.metric(
        "Average Price",
        f"₹ {df['Price'].mean():,.0f}"
    )

with col3:
    st.metric(
        "Average Mileage",
        f"{df['Mileage_Value'].mean():.2f}"
    )

with col4:
    st.metric(
        "Brands",
        df["Company_Name"].nunique()
    )

st.markdown("---")

st.info(
"""
👈 Select a page from the **Pages** folder using the sidebar navigation to explore
different analyses and business insights.
"""
)