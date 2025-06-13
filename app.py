import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set up the web app
st.set_page_config(page_title="NEPSE % Change Predictor", layout="centered")

st.title("📈 Predict NEPSE Percentage Change")
st.markdown("Provide **Index Value** and **Absolute Change** to estimate the **Percentage Change**.")

# Input fields
index_value = st.number_input("🔢 Index Value", value=2000.0, step=0.1)
absolute_change = st.number_input("📉 Absolute Change", value=10.0, step=0.1)

# Prediction logic
if st.button("Predict Percentage Change"):
    input_data = np.array([[index_value, absolute_change]])
    prediction = model.predict(input_data)[0]
    st.success(f"📊 Predicted Percentage Change: **{prediction:.2f}%**")
