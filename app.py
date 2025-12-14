# Importing libs 
import joblib 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st

# Page Config
st.set_page_config(
    page_title="Montgomery Warehouses Sales Analysis",
    page_icon="✒️",
    layout="wide"
)

# Intro 
st.title("Montgomery County Warehouses Sales Aanlysis")
with st.expander("Dataset Brief"):
    st.header("Dataset")
    st.write("""This analysis is performed for Warehouses in Montgomery County, USA about Sales. The data is provided by the Government. 
                        This dataset contains around half a million records for four years from 2017 to 2020 randomly. Not every month sales are mentioned.
                        However, the dataset is enough for performing analysis and analytics efficiently.""")

# Load data 
df_fetched_db = pd.read_csv("D:/Datasets/Liquor_Sales_USA/df_sql_nosql_concat_db.csv")

# Dashboard
# year filter
available_years = sorted(df_fetched_db["year"].unique())
selected_years = st.multiselect(
    "Select Year(s)",
    options=available_years,
    default=available_years
)

df_filtered = df_fetched_db[df_fetched_db["year"].isin(selected_years)]

fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle("Sales Dashboard", fontsize=18, fontweight="bold")

# Yearly Sales
yearly_sales = df_filtered.groupby("year")["retail sales"].sum()
axs[0, 0].plot(yearly_sales.index, yearly_sales.values, "o-b", label="Yearly Sales")
axs[0, 0].set_title("Sales by Year")
axs[0, 0].set_xlabel("Year")
axs[0, 0].set_ylabel("Sales")
axs[0, 0].grid()
axs[0, 0].legend()

# Monthly Sales
monthly_sales = df_filtered.groupby(["year", "month"])["retail sales"].sum()
month_labels = [f"{y}_{m}" for y, m in monthly_sales.index]
axs[0, 1].plot(month_labels, monthly_sales.values, "s-y", label="Monthly Sales")
axs[0, 1].set_title("Sales Monthly by Year")
axs[0, 1].set_xlabel("Months")
axs[0, 1].set_ylabel("Sales")
axs[0, 1].tick_params(axis="x", rotation=90)
axs[0, 1].grid()
axs[0, 1].legend()

# Retail Transfers
retail_transfers = df_filtered.groupby(["year", "month"])["retail transfers"].sum()
rt_labels = [f"{y}_{m}" for y, m in retail_transfers.index]
axs[1, 0].plot(rt_labels, retail_transfers.values, "d-g", label="Retail Transfers")
axs[1, 0].set_title("Retail Transfers Monthly by Year")
axs[1, 0].set_xlabel("Months")
axs[1, 0].set_ylabel("Retail Transfers")
axs[1, 0].tick_params(axis="x", rotation=90)
axs[1, 0].grid()
axs[1, 0].legend()

# Warehouse Sales
warehouse_sales = df_filtered.groupby(["year", "month"])["warehouse sales"].sum()
wh_labels = [f"{y}_{m}" for y, m in warehouse_sales.index]
axs[1, 1].plot(wh_labels, warehouse_sales.values, "^-m", label="Warehouse Sales")
axs[1, 1].set_title("Warehouse Sales Monthly by Year")
axs[1, 1].set_xlabel("Months")
axs[1, 1].set_ylabel("Warehouse Sales")
axs[1, 1].tick_params(axis="x", rotation=90)
axs[1, 1].grid()
axs[1, 1].legend()

plt.tight_layout(rect=[0, 0, 1, 0.96]) # Don't overlap (left, bottom, right, top)
st.pyplot(fig) # Put figure canvas to streamlit 

# Analytics 
st.image("resources/retail_sales_forecast.png", caption="Retail Sales Forecast", use_container_width=True)
st.image(
    "resources/retail_sales_forecast_components.png",
    caption="Forecast Components (Trend & Seasonality)",
    use_container_width=True
)

# REF:
# 1. https://docs.streamlit.io/
# 2. https://medium.com/@verinamk/streamlit-for-beginners-build-your-first-dashboard-58b764a62a2d
