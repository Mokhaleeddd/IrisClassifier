import streamlit as st
import requests

st.title("🌸 Iris Flower Classifier")
st.write("Enter the flower's features:")

# Input fields
sepal_length = st.number_input("Sepal length (cm)", value=5.1)
sepal_width = st.number_input("Sepal width (cm)", value=3.5)
petal_length = st.number_input("Petal length (cm)", value=1.4)
petal_width = st.number_input("Petal width (cm)", value=0.2)

# Predict button
if st.button("Predict"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    try:
        response = requests.post("http://127.0.0.1:5000/predict", json={"features": features})
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            target_names = ["Setosa", "Versicolor", "Virginica"]
            st.success(f"Predicted Class: {target_names[prediction]}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"⚠️ Request failed: {e}")
