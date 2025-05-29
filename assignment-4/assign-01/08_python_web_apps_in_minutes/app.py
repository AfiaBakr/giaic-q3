import streamlit as st
import joblib

model = joblib.load("linear_regression_model.pkl")

st.title("Linear Regression Prediction App")
st.write("Enter your value to get the prediction")

value = st.number_input("Enter  a vlue for the feathure:", nim_value = 0, max_value = 100, value = 2)

if st.button("Predict"):
    prediction = model.predict([[value]])
    st.write(f"the predicted target vale is {prediction[0]:.2f}")
