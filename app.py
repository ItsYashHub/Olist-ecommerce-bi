
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Olist E-Commerce Dashboard", page_icon="🛒", layout="wide")

path = r"C:\Users\jadha\task 2\\"

@st.cache_data
def load_data():
    orders = pd.read_csv(path + "orders_clean.csv")
    payments = pd.read_csv(path + "payments_clean.csv")
    order_items = pd.read_csv(path + "olist_order_items_dataset.csv")
    customers = pd.read_csv(path + "olist_customers_dataset.csv")
    reviews = pd.read_csv(path + "reviews_clean.csv")
    forecast = pd.read_csv(path + "forecast_results.csv")
    kpis = pd.read_csv(path + "kpi_summary.csv")
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"], errors="coerce")
    return orders, payments, order_items, customers, reviews, forecast, kpis

orders, payments, order_items, customers, reviews, forecast, kpis = load_data()

st.title("Olist E-Commerce Business Intelligence Dashboard")
st.markdown("---")

st.subheader("Key Performance Indicators")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Orders", f"{orders['order_id'].nunique():,}")
col2.metric("Total Revenue", f"BRL {payments['payment_value'].sum():,.0f}")
col3.metric("AOV", f"BRL {payments.groupby('order_id')['payment_value'].sum().mean():,.2f}")
col4.metric("Avg Review", f"{reviews['review_score'].mean():.2f}/5")
col5.metric("Cancel Rate", f"{(orders['order_status']=='canceled').mean()*100:.2f}%")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Monthly Revenue Trend")
    df = orders.merge(payments, on="order_id", how="left")
    df["month_year"] = df["order_purchase_timestamp"].dt.to_period("M")
    monthly = df.groupby("month_year")["payment_value"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(monthly["month_year"].astype(str), monthly["payment_value"], marker="o", color="darkorange")
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("Payment Type Distribution")
    fig, ax = plt.subplots(figsize=(8,4))
    payments["payment_type"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    plt.tight_layout()
    st.pyplot(fig)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Customer States")
    top_states = customers["customer_state"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10,4))
    top_states.plot(kind="bar", color="teal", ax=ax)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("Review Score Distribution")
    fig, ax = plt.subplots(figsize=(8,4))
    reviews["review_score"].value_counts().sort_index().plot(kind="bar", color="coral", ax=ax)
    plt.tight_layout()
    st.pyplot(fig)

st.markdown("---")
st.subheader("Sales Forecast - Next 6 Months")
st.dataframe(forecast, use_container_width=True)
st.image(path + "sales_forecast.png", use_container_width=True)

st.markdown("---")
st.subheader("Business KPI Summary")
st.dataframe(kpis, use_container_width=True)
