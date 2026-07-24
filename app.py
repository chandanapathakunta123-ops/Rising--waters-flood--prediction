import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="🌊 Flood Risk Prediction", layout="centered")

st.title("🌊 Rising Waters - Flood Risk Prediction")
st.write("Enter details to check flood risk")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_excel("flood_dataset.xlsx")
    return df

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Load model
model = joblib.load("flood_model.pkl")

st.subheader("Make a Prediction")
st.write("Fill all 10 fields based on your dataset")

# 10 Input fields - same order as training
temp = st.number_input("Temp", min_value=0.0, value=29.0)
humidity = st.number_input("Humidity", min_value=0.0, value=70.0)
cloud = st.number_input("Cloud Cover", min_value=0.0, value=30.0)
annual = st.number_input("ANNUAL", min_value=0.0, value=3248.6)
jan_feb = st.number_input("Jan-Feb", min_value=0.0, value=50.0)
mar_may = st.number_input("Mar-May", min_value=0.0, value=200.0)
jun_sep = st.number_input("Jun-Sep", min_value=0.0, value=2500.0)
oct_dec = st.number_input("Oct-Dec", min_value=0.0, value=400.0)
avg_june = st.number_input("avgjune", min_value=0.0, value=300.0)
sub = st.number_input("sub", min_value=0.0, value=100.0)

if st.button("Predict"):
    input_data = np.array([[temp, humidity, cloud, annual, jan_feb, mar_may, jun_sep, oct_dec, avg_june, sub]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🚨 Flood Risk: HIGH")
    else:
        st.success("✅ Flood Risk: LOW")
