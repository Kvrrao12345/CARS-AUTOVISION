import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path



st.set_page_config(
    page_title="Exploratory Data Analysis",
    layout="wide"
)


@st.cache_data
def load_data():
    return pd.read_csv("cars_clean.xls")

df = load_data()


st.title("Exploratory Data Analysis")

st.markdown(
"""
Explore the dataset using interactive charts and business-focused insights.
"""
)

st.markdown("---")

st.sidebar.header("Filters")

brand = st.sidebar.multiselect(
    "Select Brand",
    sorted(df["Company_Name"].dropna().unique()),
    default=sorted(df["Company_Name"].dropna().unique())
)

fuel = st.sidebar.multiselect(
    "Fuel Type",
    sorted(df["Fuel_Type"].dropna().unique()),
    default=sorted(df["Fuel_Type"].dropna().unique())
)

transmission = st.sidebar.multiselect(
    "Transmission",
    sorted(df["Transmission"].dropna().unique()),
    default=sorted(df["Transmission"].dropna().unique())
)

filtered_df = df[
    (df["Company_Name"].isin(brand)) &
    (df["Fuel_Type"].isin(fuel)) &
    (df["Transmission"].isin(transmission))
]


st.subheader("Dataset Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", len(filtered_df))
c2.metric("Columns", filtered_df.shape[1])
c3.metric("Brands", filtered_df["Company_Name"].nunique())
c4.metric("Cities", filtered_df["Location"].nunique())

st.markdown("---")


st.subheader("Missing Values")

missing = filtered_df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

if len(missing) > 0:

    fig = px.bar(
        x=missing.index,
        y=missing.values,
        labels={"x": "Columns", "y": "Missing Values"},
        title="Missing Values"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.success("No Missing Values Found")

st.markdown("---")


st.subheader("Price Distribution")

fig = px.histogram(
    filtered_df,
    x="Price",
    nbins=40,
    title="Distribution of Car Prices"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Top 10 Brands")

brand_count = (
    filtered_df["Company_Name"]
    .value_counts()
    .head(10)
    .reset_index()
)

brand_count.columns = ["Brand", "Cars"]

fig = px.bar(
    brand_count,
    x="Brand",
    y="Cars",
    color="Cars",
    title="Top Brands"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Fuel Type Distribution")

fig = px.pie(
    filtered_df,
    names="Fuel_Type",
    hole=0.5,
    title="Fuel Type Share"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Transmission Distribution")

fig = px.pie(
    filtered_df,
    names="Transmission",
    hole=0.5,
    title="Transmission Share"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Cars by Manufacturing Year")

year_df = (
    filtered_df["Year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

year_df.columns = ["Year", "Cars"]

fig = px.line(
    year_df,
    x="Year",
    y="Cars",
    markers=True,
    title="Manufacturing Year Trend"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Price vs Mileage")

fig = px.scatter(
    filtered_df,
    x="Mileage_Value",
    y="Price",
    color="Fuel_Type",
    hover_data=["Company_Name", "Model"],
    title="Price vs Mileage"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Engine vs Power")

fig = px.scatter(
    filtered_df,
    x="Engine_Value",
    y="Power_Value",
    color="Transmission",
    hover_data=["Company_Name", "Model"],
    title="Engine Capacity vs Power"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Correlation Matrix")

corr = filtered_df[
    [
        "Price",
        "Kilometers_Driven",
        "Mileage_Value",
        "Engine_Value",
        "Power_Value",
        "Seats"
    ]
].corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Heatmap"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Dataset Preview")

st.dataframe(
    filtered_df,
    use_container_width=True
)