import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Analysis Dashboard")
st.write("Interactive dashboard for product sales analysis.")

df = pd.read_csv("w7d5_sales.csv")

st.subheader("Dataset")

st.dataframe(df, use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"{df['Sales'].sum():,.0f}")

with col2:
    st.metric("Total Quantity", f"{df['Quantity'].sum():,.0f}")

with col3:
    st.metric("Products", len(df))

st.subheader("Sales by Product")

st.bar_chart(
    df.set_index("Product")["Sales"]
)

st.subheader("Quantity by Product")

st.bar_chart(
    df.set_index("Product")["Quantity"]
)

st.subheader("Category Summary")

category_summary = df.groupby("Category")[["Sales", "Quantity"]].sum()

st.dataframe(category_summary, use_container_width=True)