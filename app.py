import streamlit as st
import pickle
import numpy as np

# Load the model
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# Title
st.title("Stock Index Change Predictor")

# Input
index_value = st.number_input("Enter Index Value", format="%.4f")

# Predict button
if st.button("Predict Actual Change"):
    input_array = np.array([[index_value]])
    prediction = model.predict(input_array)
    st.success(f"Predicted Actual Change: {prediction[0]:.4f}")
