import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# Title
st.title("Market Movement Predictor")
st.write("Enter the current Index Value to predict if the market will increase tomorrow.")

# User input
index_value = st.number_input("Index Value", format="%.4f")

# Predict button
if st.button("Predict"):
    try:
        input_array = np.array([[index_value]])
        prediction = model.predict(input_array)[0]

        if prediction > 0:
            st.success(f"✅ Tomorrow will be an **Increase** (Predicted Change: {prediction:.4f})")
        elif prediction < 0:
            st.error(f"🔻 Tomorrow will be a **Decrease** (Predicted Change: {prediction:.4f})")
        else:
            st.info("➖ No Change Expected (Predicted Change: 0.0000)")
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
