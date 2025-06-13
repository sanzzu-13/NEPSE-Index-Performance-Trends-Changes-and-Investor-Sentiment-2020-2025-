import streamlit as st
import pickle
import numpy as np

# Load the trained Random Forest model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.set_page_config(page_title="NEPSE Prediction App", layout="centered")

st.title("📈 NEPSE Actual Change Predictor")
st.write("Enter the **Index Value** and **Absolute Change** to predict the Actual Change value.")

# Input fields
index_value = st.number_input("Index Value", value=2000.0, step=0.1)
absolute_change = st.number_input("Absolute Change", value=10.0, step=0.1)

# Predict
if st.button("Predict Actual Change"):
    input_data = np.array([[index_value, absolute_change]])
    prediction = model.predict(input_data)[0]
    st.success(f"📊 Predicted Actual Change: **{prediction:.2f}**")

