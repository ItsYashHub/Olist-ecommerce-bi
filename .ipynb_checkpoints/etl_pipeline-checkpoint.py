import pandas as pd
import sqlite3
from datetime import datetime

path = r"C:\Users\jadha\task 2\\"
log_file = path + "etl_log.txt"

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] {msg}"
    print(log_msg)
    with open(log_file, "a") as f:
        f.write(log_msg + "\n")

def extract():
    log("EXTRACT: Starting...")
    orders = pd.read_csv(path + "olist_orders_dataset.csv")
    payments = pd.read_csv(path + "olist_order_payments_dataset.csv")
    order_items = pd.read_csv(path + "olist_order_items_dataset.csv")
    customers = pd.read_csv(path + "olist_customers_dataset.csv")
    reviews = pd.read_csv(path + "olist_order_reviews_dataset.csv")
    products = pd.read_csv(path + "olist_products_dataset.csv")
    log(f"EXTRACT: Done - {len(orders)} orders loaded")
    return orders, payments, order_items, customers, reviews, products

def transform(orders, payments, order_items, customers, reviews, products):
    log("TRANSFORM: Cleaning...")
    orders.drop_duplicates(inplace=True)
    payments.drop_duplicates(inplace=True)
    orders["order_approved_at"].fillna(orders["order_approved_at"].mode()[0], inplace=True)
    orders["order_delivered_carrier_date"].fillna("Unknown", inplace=True)
    orders["order_delivered_customer_date"].fillna("Unknown", inplace=True)
    products["product_category_name"].fillna("unknown", inplace=True)
    products.fillna(0, inplace=True)
    reviews["review_comment_title"].fillna("No Title", inplace=True)
    reviews["review_comment_message"].fillna("No Comment", inplace=True)
    for col in ["order_purchase_timestamp","order_approved_at",
                "order_delivered_customer_date","order_estimated_delivery_date"]:
        orders[col] = pd.to_datetime(orders[col], errors="coerce")
    Q1 = payments["payment_value"].quantile(0.25)
    Q3 = payments["payment_value"].quantile(0.75)
    IQR = Q3 - Q1
    payments = payments[
        (payments["payment_value"] >= Q1-1.5*IQR) &
        (payments["payment_value"] <= Q3+1.5*IQR)
    ]
    log("TRANSFORM: Done")
    return orders, payments, order_items, customers, reviews, products

def load(orders, payments, order_items, customers, reviews, products):
    log("LOAD: Saving files...")
    orders.to_csv(path + "orders_clean.csv", index=False)
    payments.to_csv(path + "payments_clean.csv", index=False)
    products.to_csv(path + "products_clean.csv", index=False)
    reviews.to_csv(path + "reviews_clean.csv", index=False)
    conn = sqlite3.connect(path + "olist.db")
    orders.to_sql("orders", conn, if_exists="replace", index=False)
    payments.to_sql("payments", conn, if_exists="replace", index=False)
    order_items.to_sql("order_items", conn, if_exists="replace", index=False)
    customers.to_sql("customers", conn, if_exists="replace", index=False)
    conn.close()
    log("LOAD: Done")

log("===== ETL PIPELINE STARTED =====")
orders, payments, order_items, customers, reviews, products = extract()
orders, payments, order_items, customers, reviews, products = transform(orders, payments, order_items, customers, reviews, products)
load(orders, payments, order_items, customers, reviews, products)
log("===== ETL PIPELINE COMPLETED =====")
