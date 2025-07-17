import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Step 1: Load the dataset
print("[INFO] Loading Iris dataset...")
data = load_iris()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(data.data, data.target, test_size=0.3, random_state=42)

# Step 2: Train the model
print("[INFO] Training SVM model...")
model = SVC(kernel='rbf', C=1, gamma='scale')
model.fit(Xtrain, Ytrain)

# Step 3: Save the model
model_path = "model.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"[SUCCESS] Model saved to '{model_path}'")
