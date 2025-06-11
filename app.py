import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Random Forest Predictor")

st.write("Enter input features below:")

# You can change the number of features as needed
feature1 = st.number_input("Feature 1", step=0.1)
feature2 = st.number_input("Feature 2", step=0.1)
feature3 = st.number_input("Feature 3", step=0.1)
feature4 = st.number_input("Feature 4", step=0.1)

# Button for prediction
if st.button("Predict"):
    input_data = np.array([[feature1, feature2, feature3, feature4]])
    prediction = model.predict(input_data)
    st.success(f"Prediction: {prediction[0]}")
