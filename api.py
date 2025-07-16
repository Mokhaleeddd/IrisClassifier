from flask import Flask, request, jsonify
import numpy as np
import pickle

# Load your trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Iris prediction API!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array([[ 
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]])
    prediction = model.predict(features)
    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
