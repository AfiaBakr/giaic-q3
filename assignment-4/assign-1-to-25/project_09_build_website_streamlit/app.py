import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Data Filter")
    columns = df.columns.to_list()
    selected_col = st.selectbox("Select column to filter by", columns)
    unique_value = df[selected_col].unique()
    selected_value = st.selectbox("Select Value", unique_value)

    filter_df = df[df[selected_col] == selected_value]
    st.write(filter_df)

    st.subheader("Plot Data")
    x_col = st.selectbox("Select X-axis Column", columns)
    y_col = st.selectbox("Select Y-axis Column", columns)

    if st.button("Generate Plot"):
        try:
            st.line_chart(filter_df.set_index(x_col)[y_col])
        except Exception as e:
            st.error(f"Error generating chart: {e}")
else:
    st.write("Waiting on file uploading....")

st.markdown("Created by Afia Bakr")
