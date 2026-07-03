# ==========================================
# DecodeLabs AI Project 2
# AI Data Classification
# Developed by: Nadendla Sai Vyshnavi
# ==========================================

# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print("=" * 60)
print("      AI FLOWER CLASSIFICATION SYSTEM")
print("=" * 60)

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Loaded Successfully")
print("Total Samples :", len(X))
print("Features :", iris.feature_names)
print("Classes :", iris.target_names)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nDataset Split Completed")
print("Training Samples :", len(X_train))
print("Testing Samples :", len(X_test))

# Create AI Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X_train, y_train)

print("\nModel Training Completed Successfully")

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy : {:.2f}%".format(accuracy * 100))

print("\nPredictions")

for i in range(len(predictions)):
    actual = iris.target_names[y_test[i]]
    predicted = iris.target_names[predictions[i]]

    print(f"Flower {i+1}")
    print("Actual     :", actual)
    print("Predicted  :", predicted)
    print("-" * 30)

print("\nProject Completed Successfully")