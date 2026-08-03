import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path



st.set_page_config(
    page_title="Business Insights",
    layout="wide"
)


@st.cache_data
def load_data():
    return pd.read_csv("cars_clean.xls")

df = load_data()


st.title("Business Insights")
st.markdown("Actionable insights derived from the used car dataset.")

st.markdown("---")


c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Average Price",
        f"₹ {df['Price'].mean():,.0f}"
    )

with c2:
    st.metric(
        "Average Mileage",
        f"{df['Mileage_Value'].mean():.2f}"
    )

with c3:
    st.metric(
        "Average Engine",
        f"{df['Engine_Value'].mean():.0f} cc"
    )

with c4:
    st.metric(
        "Average Power",
        f"{df['Power_Value'].mean():.0f} bhp"
    )

st.markdown("---")


brand_price = (
    df.groupby("Company_Name")["Price"]
    .mean()
    .sort_values(ascending=False)
)

highest_brand = brand_price.index[0]
lowest_brand = brand_price.index[-1]

popular_brand = df["Company_Name"].value_counts().idxmax()


popular_fuel = df["Fuel_Type"].mode()[0]


popular_transmission = df["Transmission"].mode()[0]


city_price = (
    df.groupby("Location")["Price"]
    .mean()
    .sort_values(ascending=False)
)

highest_city = city_price.index[0]


best_mileage = (
    df.groupby("Company_Name")["Mileage_Value"]
    .mean()
    .sort_values(ascending=False)
)

best_mileage_brand = best_mileage.index[0]


st.header("Key Business Insights")

st.success(f"""
 **{highest_brand}** has the highest average selling price.
""")

st.info(f"""
**{popular_brand}** has the largest number of cars listed in the dataset.
""")

st.warning(f"""
**{lowest_brand}** has the lowest average selling price.
""")

st.success(f"""
           **{popular_fuel}** is the most preferred fuel type among buyers.
""")

st.info(f"""
⚙ **{popular_transmission}** is the most common transmission type.
""")

st.success(f"""
           **{highest_city}** has the highest average vehicle price.
""")

st.info(f"""
        **{best_mileage_brand}** offers the highest average mileage.
""")

st.markdown("---")


st.subheader("Average Price by Brand")

brand_df = (
    df.groupby("Company_Name")["Price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    brand_df,
    x="Company_Name",
    y="Price",
    color="Price",
    title="Top 10 Most Expensive Brands"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Fuel Type Market Share")

fig = px.pie(
    df,
    names="Fuel_Type",
    hole=0.45,
    title="Fuel Type Distribution"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Transmission Preference")

fig = px.bar(
    df["Transmission"].value_counts().reset_index(),
    x="Transmission",
    y="count",
    color="count",
    title="Transmission Distribution"
)

st.plotly_chart(fig, use_container_width=True)


st.header("Business Recommendations")

st.markdown("""
### Recommendation 1
Focus inventory on brands with consistently high resale values, as they tend to generate greater returns.

### Recommendation 2
Maintain a balanced stock of petrol, diesel, and other fuel variants according to customer demand.

### Recommendation 3
Automatic transmission vehicles continue to gain popularity and should be considered when expanding inventory.

### Recommendation 4
Highlight vehicles with low kilometers driven and complete service history, as they generally command higher prices.

### Recommendation 5
Use regional pricing insights to identify cities with stronger resale markets and optimize inventory allocation.
""")

st.markdown("---")


st.header("Dashboard Summary")

st.write("""
This analysis provides a comprehensive overview of the used car market by
examining pricing, brand performance, fuel preferences, transmission trends,
and regional variations. These insights can support data-driven decisions for
dealerships, buyers, sellers, and market analysts.
""")