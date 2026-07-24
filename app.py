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

# Input fields - nee dataset columns batti marchu
monsoon = st.number_input("MonsoonIntensity", min_value=0.0)
topography = st.number_input("Topography", min_value=0.0)
river = st.number_input("RiverManagement", min_value=0.0)

if st.button("Predict"):
    input_data = np.array([[monsoon, topography, river]])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("🚨 Flood Risk: HIGH")
    else:
        st.success("✅ Flood Risk: LOW")
