{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3c4b440f-ccef-4e52-ac1c-4f112bcecbcc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\data python\\lib\\site-packages (1.32.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\data python\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\data python\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\data python\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\data python\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\data python\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\data python\\lib\\site-packages (from streamlit) (23.2)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\data python\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\data python\\lib\\site-packages (from streamlit) (10.3.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\data python\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\data python\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\data python\\lib\\site-packages (from streamlit) (2.32.2)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\data python\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\data python\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\data python\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\data python\\lib\\site-packages (from streamlit) (4.15.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\data python\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\data python\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\data python\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\data python\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: jinja2 in c:\\data python\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\data python\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in c:\\data python\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\data python\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\data python\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\data python\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\data python\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\data python\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\data python\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\data python\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\data python\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.6.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\data python\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2026.4.22)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in c:\\data python\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\data python\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\data python\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\data python\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\data python\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (26.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\data python\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\data python\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\data python\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\data python\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\data python\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dca41fff-e9c3-4874-8a34-96117bba6109",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "app.py created ✅\n"
     ]
    }
   ],
   "source": [
    "app_code = '''\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "st.set_page_config(page_title=\"Olist E-Commerce Dashboard\", page_icon=\"🛒\", layout=\"wide\")\n",
    "\n",
    "path = r\"C:\\\\Users\\\\jadha\\\\task 2\\\\\\\\\"\n",
    "\n",
    "@st.cache_data\n",
    "def load_data():\n",
    "    orders = pd.read_csv(path + \"orders_clean.csv\")\n",
    "    payments = pd.read_csv(path + \"payments_clean.csv\")\n",
    "    order_items = pd.read_csv(path + \"olist_order_items_dataset.csv\")\n",
    "    customers = pd.read_csv(path + \"olist_customers_dataset.csv\")\n",
    "    reviews = pd.read_csv(path + \"reviews_clean.csv\")\n",
    "    forecast = pd.read_csv(path + \"forecast_results.csv\")\n",
    "    kpis = pd.read_csv(path + \"kpi_summary.csv\")\n",
    "    orders[\"order_purchase_timestamp\"] = pd.to_datetime(orders[\"order_purchase_timestamp\"], errors=\"coerce\")\n",
    "    return orders, payments, order_items, customers, reviews, forecast, kpis\n",
    "\n",
    "orders, payments, order_items, customers, reviews, forecast, kpis = load_data()\n",
    "\n",
    "st.title(\"Olist E-Commerce Business Intelligence Dashboard\")\n",
    "st.markdown(\"---\")\n",
    "\n",
    "st.subheader(\"Key Performance Indicators\")\n",
    "col1, col2, col3, col4, col5 = st.columns(5)\n",
    "col1.metric(\"Total Orders\", f\"{orders['order_id'].nunique():,}\")\n",
    "col2.metric(\"Total Revenue\", f\"BRL {payments['payment_value'].sum():,.0f}\")\n",
    "col3.metric(\"AOV\", f\"BRL {payments.groupby('order_id')['payment_value'].sum().mean():,.2f}\")\n",
    "col4.metric(\"Avg Review\", f\"{reviews['review_score'].mean():.2f}/5\")\n",
    "col5.metric(\"Cancel Rate\", f\"{(orders['order_status']=='canceled').mean()*100:.2f}%\")\n",
    "\n",
    "st.markdown(\"---\")\n",
    "\n",
    "col1, col2 = st.columns(2)\n",
    "\n",
    "with col1:\n",
    "    st.subheader(\"Monthly Revenue Trend\")\n",
    "    df = orders.merge(payments, on=\"order_id\", how=\"left\")\n",
    "    df[\"month_year\"] = df[\"order_purchase_timestamp\"].dt.to_period(\"M\")\n",
    "    monthly = df.groupby(\"month_year\")[\"payment_value\"].sum().reset_index()\n",
    "    fig, ax = plt.subplots(figsize=(10,4))\n",
    "    ax.plot(monthly[\"month_year\"].astype(str), monthly[\"payment_value\"], marker=\"o\", color=\"darkorange\")\n",
    "    plt.xticks(rotation=90)\n",
    "    plt.tight_layout()\n",
    "    st.pyplot(fig)\n",
    "\n",
    "with col2:\n",
    "    st.subheader(\"Payment Type Distribution\")\n",
    "    fig, ax = plt.subplots(figsize=(8,4))\n",
    "    payments[\"payment_type\"].value_counts().plot(kind=\"pie\", autopct=\"%1.1f%%\", ax=ax)\n",
    "    ax.set_ylabel(\"\")\n",
    "    plt.tight_layout()\n",
    "    st.pyplot(fig)\n",
    "\n",
    "st.markdown(\"---\")\n",
    "\n",
    "col1, col2 = st.columns(2)\n",
    "\n",
    "with col1:\n",
    "    st.subheader(\"Top 10 Customer States\")\n",
    "    top_states = customers[\"customer_state\"].value_counts().head(10)\n",
    "    fig, ax = plt.subplots(figsize=(10,4))\n",
    "    top_states.plot(kind=\"bar\", color=\"teal\", ax=ax)\n",
    "    plt.xticks(rotation=45)\n",
    "    plt.tight_layout()\n",
    "    st.pyplot(fig)\n",
    "\n",
    "with col2:\n",
    "    st.subheader(\"Review Score Distribution\")\n",
    "    fig, ax = plt.subplots(figsize=(8,4))\n",
    "    reviews[\"review_score\"].value_counts().sort_index().plot(kind=\"bar\", color=\"coral\", ax=ax)\n",
    "    plt.tight_layout()\n",
    "    st.pyplot(fig)\n",
    "\n",
    "st.markdown(\"---\")\n",
    "st.subheader(\"Sales Forecast - Next 6 Months\")\n",
    "st.dataframe(forecast, use_container_width=True)\n",
    "st.image(path + \"sales_forecast.png\", use_container_width=True)\n",
    "\n",
    "st.markdown(\"---\")\n",
    "st.subheader(\"Business KPI Summary\")\n",
    "st.dataframe(kpis, use_container_width=True)\n",
    "'''\n",
    "\n",
    "with open(r\"C:\\Users\\jadha\\task 2\\app.py\", \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(app_code)\n",
    "\n",
    "print(\"app.py created ✅\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "eaa99721-6227-4880-a777-5e5f93c6c0bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Streamlit running at: http://localhost:8501 ✅\n",
      "Open browser and go to: http://localhost:8501\n"
     ]
    }
   ],
   "source": [
    "import subprocess\n",
    "subprocess.Popen([\"streamlit\", \"run\", r\"C:\\Users\\jadha\\task 2\\app.py\"])\n",
    "print(\"Streamlit running at: http://localhost:8501 ✅\")\n",
    "print(\"Open browser and go to: http://localhost:8501\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b9cebe1-7add-4517-b1c2-dc47a5efe014",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
