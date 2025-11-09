# 📈 Sales Forecasting Web Dashboard  

### 🚀 *Predicting future retail sales through data-driven insights using Python, Time Series Analysis, and Streamlit.*

---

![Dashboard Banner](https://github.com/yourusername/sales-forecasting-dashboard/assets/banner_image.png)

---

## 🧭 Table of Contents  
1. [📘 Project Description / Purpose](#-project-description--purpose)  
2. [🧰 Tech Stack](#-tech-stack)  
3. [📊 Data Source](#-data-source)  
4. [💡 Features & Highlights](#-features--highlights)  
5. [🧠 Methodology](#-methodology)  
6. [🖼️ Dashboard Screenshots](#️-dashboard-screenshots)  
7. [⚙️ How to Run the Project](#️-how-to-run-the-project)  
8. [🚀 Future Enhancements](#-future-enhancements)  
9. [👨‍💻 Author](#-author)  

---

## 📘 Project Description / Purpose  

The **Sales Forecasting Web Dashboard** is a data-driven analytical application built to **predict future retail sales** using historical data.  
It enables businesses to **optimize inventory, plan promotions**, and **make data-backed decisions** by visualizing patterns, seasonality, and forecasts interactively.

Key capabilities:
- Data preprocessing and cleaning (12K+ rows)
- Time series analysis using **ARIMA/SARIMA**
- Interactive **Streamlit dashboard** for real-time exploration

---

## 🧰 Tech Stack  

| Category | Technologies |
|-----------|--------------|
| **Programming Language** | Python |
| **Data Analysis** | pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Modeling** | statsmodels (ARIMA/SARIMA), ADF, KPSS |
| **Dashboard** | Streamlit |
| **Version Control** | Git & GitHub |

---

## 📊 Data Source 


## 📊 Data Source  

This project uses a **sample retail transaction dataset** simulating real-world daily sales records.  
It includes details such as product category, item, price, sales quantity, total spent, customer location, and payment method.

- **Dataset:** Historical retail sales data (~12,000 rows)  
- **Attributes:** Date, Store, Item, Sales, Promotions  
- **Scope:** Daily/weekly sales from multiple store categories  
- **Source Type:** Internal / Kaggle dataset 


### 🧩 Data Overview  
- **Rows:** 10 (sample from full dataset of ~12K records)  
- **Columns:** 11  
- **Features include:**  
  - `Transaction ID`, `Customer ID` — unique identifiers  
  - `Category`, `Item`, `Price`, `Total Sale`, `Total Spent` — sales metrics  
  - `Payment Method`, `Location`, `Date`, `Discount Applied` — contextual data  

### ⚙️ Cleaning Performed  
- Handled missing values in `Item`, `Price Per Unit`, and `Discount Applied` for data accuracy.  
- Recomputed `Total Spent` using **`Total Spent = Price Per Unit × Total Sale`** to fix inconsistencies.  
- Filled missing `Discount Applied` with `False` and inferred missing `Item` names within each `Category`.  
- Converted `Date` to datetime format, extracted time-based features, and aggregated daily sales for forecasting.  


---



 

---

## 💡 Features & Highlights  

### 🧩 Business Problem  
Retail firms face fluctuating demand and uncertainty in inventory management.  
This project provides a **data-driven forecasting tool** to improve planning accuracy.

### 🎯 Goal of the Dashboard  
- Analyze historical sales patterns  
- Detect **trend, seasonality, autocorrelation**  
- Build **ARIMA/SARIMA models** for reliable forecasts  
- Present results through an **interactive dashboard**

---

### 🔍 Walkthrough of Key Visuals  

| Visual | Description |
|--------|--------------|
| **Time Series Decomposition** | Displays trend, seasonality, and residuals |
| **ACF/PACF Analysis** | Identifies AR and MA terms for ARIMA model |
| **Model Comparison Panel** | Evaluates ARIMA vs SARIMA accuracy |
| **Forecast Plot** | Visualizes future sales vs actuals |
| **Data Insights View** | Allows filtering by store or product |

---

### 📈 Business Impact & Insights  

✅ Improved forecast accuracy  
✅ Optimized inventory management  
✅ Enhanced understanding of seasonality  
✅ Empowered business teams with interactive insights  

---

## 🧠 Methodology  

1. **Data Cleaning**  
   - Removed missing values & outliers  
   - Created date-based features (month, week, day)  

2. **Exploratory Data Analysis (EDA)**  
   - Trend & seasonality decomposition  
   - ACF/PACF for parameter tuning  
   - Stationarity tests (ADF & KPSS)  

3. **Model Development**  
   - Built ARIMA/SARIMA models  
   - Evaluated with RMSE & MAPE  

4. **Dashboard Deployment**  
   - Streamlit interface for real-time forecasting visualization  

---

## 🖼️ Dashboard Screenshots  

### 🔹 Dashboard Home  
![Dashboard Overview](sandbox:/mnt/data/dashboard_page_1.png)

### 🔹 Forecast Visualization  
![Forecast Chart](sandbox:/mnt/data/dashboard_page_2.png)

### 🔹 Trend & Seasonality  
![Trend Analysis](sandbox:/mnt/data/dashboard_page_3.png)

---

## ⚙️ How to Run the Project  

### 🧩 Prerequisites  
```bash
Python 3.8+
pip install -r requirements.txt
