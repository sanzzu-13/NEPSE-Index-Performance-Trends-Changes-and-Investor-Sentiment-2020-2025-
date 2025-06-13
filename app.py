import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.set_page_config(page_title="NEPSE Price Predictor", page_icon="📊")
st.title("📈 NEPSE Tomorrow Prediction")
st.subheader("Will the market increase tomorrow? Let's find out!")

# User inputs
index_value = st.number_input("Enter today's Index Value", format="%.2f")
absolute_change = st.number_input("Enter today's Absolute Change", format="%.2f")

# Prediction logic
if st.button("Predict"):
    input_data = np.array([[index_value, absolute_change]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Yes! The market is likely to go UP tomorrow 🚀📈")
    else:
        st.error("No! The market might go DOWN tomorrow 😢📉")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Susmi and Baby")
