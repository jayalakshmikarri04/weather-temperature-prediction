import streamlit as st
import numpy as np
import joblib

# Load saved model
model = joblib.load("polynomial_temperature_model.pkl")

# App title
st.title("🌡️ Temperature Prediction App")
st.write("Predict **Maximum Temperature** using Polynomial Regression")

# User inputs
temp_min = st.number_input("Enter Minimum Temperature (°C)", value=5.0)
precipitation = st.number_input("Enter Precipitation (mm)", value=1.0)

# Predict button
if st.button("Predict Temperature"):
    input_data = np.array([[temp_min, precipitation]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Maximum Temperature: {prediction[0]:.2f} °C")
