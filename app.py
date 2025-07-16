import requests
import streamlit as st

sepal_length = st.number_input("Sepal length")
sepal_width = st.number_input("Sepal width")
petal_length = st.number_input("Petal length")
petal_width = st.number_input("Petal width")

if st.button("Predict"):
    url = "http://127.0.0.1:5000/predict"
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    response = requests.post(url, json=payload)
    st.write("Prediction:", response.json()["prediction"])
