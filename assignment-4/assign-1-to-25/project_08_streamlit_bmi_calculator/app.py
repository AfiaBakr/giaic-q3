import streamlit as st
import pandas as pd

st.title('BMI Calculator')
height = st.slider("Enter your height (in cm)", 100,250,175)
weight = st.slider("Enter your weight (in kg)", 40,200,70)

bmi = weight / ((height/100)**2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("Underweight : BMI lessthen 18.5")
st.write("Normal weight : BMI between  18.5 to 24.9")
st.write("Overweight : BMI between  25 to 29.9")
st.write("Obesity : BMI 30 or greater")


st.markdown("<h4 style='text-align: center; color: grey;'>Created by Afia Bakr</h4>", unsafe_allow_html=True)

