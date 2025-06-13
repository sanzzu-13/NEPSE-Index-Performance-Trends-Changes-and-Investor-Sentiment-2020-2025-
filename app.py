import streamlit as st
import pickle
import numpy as np

# Load the saved Random Forest Classifier model
with open('random_forest_classifier.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Tomorrow's Increase Prediction")

st.write("Enter today's data to predict if tomorrow's value will increase or not.")

# Input fields for features
index_value = st.number_input("Index Value", value=0.0)
absolute_change = st.number_input("Absolute Change", value=0.0)

# Predict button
if st.button("Predict"):
    # Prepare input data for prediction
    input_data = np.array([[index_value, absolute_change]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Show result
    if prediction == 1:
        st.success("Prediction: Tomorrow's value WILL increase 📈")
    else:
        st.error("Prediction: Tomorrow's value will NOT increase 📉")
