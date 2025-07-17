# 🌸 IrisClassifier

This project classifies the Iris dataset using a machine learning model (SVC), served through a Flask API and integrated with a Streamlit frontend for interaction.

---

## 📁 Project Structure

```
IrisClassifier/
│
├── app.py              # Flask API backend
├── api.py              # Streamlit frontend
├── model.pkl           # Trained SVC model
├── iris_model.pkl      # Optional saved model
├── README.md           # Project documentation
└── requirements.txt    # Dependencies
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mokhaleeddd/IrisClassifier.git
   cd IrisClassifier
   ```

2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧠 Model Training (Already Done)

The model is trained on the Iris dataset using `SVC (Support Vector Classifier)` with `RBF` kernel:

```python
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pickle

data = load_iris()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(data.data, data.target, test_size=0.3, random_state=42)
model = SVC(kernel='rbf', C=1, gamma='scale')
model.fit(Xtrain, Ytrain)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
```

---

## 🚀 Run the Flask API

```bash
python app.py
```

The API will run at: `http://127.0.0.1:5000`

### Available endpoints:
- `GET /` — returns a welcome message.
- `POST /predict` — accepts a JSON payload with features and returns prediction.

**Example JSON:**
```json
{
  "sepal_length": 6.4,
  "sepal_width": 3.2,
  "petal_length": 4.5,
  "petal_width": 1.5
}
```

---

## 💻 Run the Streamlit Frontend

```bash
streamlit run api.py
```

This will launch an interactive UI in your browser to enter input features and see predictions in real-time.

---

## 🧪 Sample Prediction (Python)

```python
import pickle
sample = [[6.4, 3.2, 4.5, 1.5]]
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
prediction = model.predict(sample)
print("Predicted class:", prediction)
```

---

## ✅ Requirements

`requirements.txt` should include:

```
flask
streamlit
scikit-learn
numpy
pandas
```

---

## 📌 Notes

- Make sure `model.pkl` exists in the same directory before running the API.
- Ensure your Flask server is running **before** using the Streamlit app.
- This project uses Python 3.9+ and scikit-learn 1.6+.

---

## 🔗 GitHub Repository

[https://github.com/mokhaleeddd/IrisClassifier](https://github.com/mokhaleeddd/IrisClassifier)