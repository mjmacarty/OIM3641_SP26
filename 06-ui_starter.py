from datetime import date, timedelta
import pandas as pd
import plotly.express as px
import streamlit as st
import yfinance as yf

# CONSTANTS
END = date.today()
START = END - timedelta(365)

# data handling
def get_stock_data(ticker, start, end):
    try:
        data = yf.download(ticker, start, end, auto_adjust=False)
        if data.empty:
            return None, f"No data found for {ticker}"
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
        return data, f"Successfully loaded data for {ticker}"
    except Exception as e:
        return None, f"Error {e}"
