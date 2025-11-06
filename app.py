import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

st.title("Sales Forecasting Dashboard")

uploaded_file = st.file_uploader("retail_store_sales.cvs", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file, parse_dates=['Date'])
    data.set_index('Date', inplace=True)
    
    st.subheader("Raw Data")
    st.line_chart(data['Total Sale'])

    # Fit basic ARIMA model
    model = ARIMA(data['Total Sale'], order=(5,1,2))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=30)

    st.subheader("Forecast")
    fig, ax = plt.subplots()
    ax.plot(data.index, data['Total Sale'], label="Historic")
    ax.plot(pd.date_range(data.index[-1], periods=30, freq='D'), forecast, label="Forecast")
    ax.legend()
    st.pyplot(fig)
