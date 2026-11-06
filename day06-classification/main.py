import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# Import Matplotlib
import matplotlib.pyplot as plt
# Import ConfusionMatrixDisplay
from sklearn.metrics import ConfusionMatrixDisplay
# Import evaluation functions
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# Import NumPy for numerical operations
import numpy as np
# Create a developer dataset
data = {
    "experience": [
        1, 2, 1, 3, 2,
        4, 5, 3, 6, 4,
        2, 5, 7, 3, 6,
        1, 4, 5, 7, 8
    ],
    "coding_score": [
        30, 45, 35, 65, 50,
        75, 90, 70, 85, 80,
        40, 88, 95, 60, 92,
        25, 78, 85, 98, 96
    ],
    "projects": [
        1, 2, 1, 3, 2,
        4, 6, 3, 5, 4,
        2, 5, 7, 3, 6,
        1, 4, 5, 8, 9
    ],
    "technical_score": [
        35, 40, 30, 65, 45,
        75, 92, 68, 88, 80,
        38, 90, 95, 62, 94,
        25, 78, 86, 98, 97
    ],
    "interview_result": [
        0, 0, 0, 1, 0,
        1, 1, 1, 1, 1,
        0, 1, 1, 1, 1,
        0, 1, 1, 1, 1
    ]
}
# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)
# Display the complete dataset
print(df)
# Display dataset information
print(df.info())
# Display statistical information
print(df.describe())

# X = Experience, Coding Score, Projects, Technical Score.
# y = Interview Result.


# Select input features
X = df[
    [
        "experience",
        "coding_score",
        "projects",
        "technical_score"
    ]
]

# Select the target variable
y = df["interview_result"]
# Display input features
print("Features:")
print(X.head())
# Display target values
print("Target:")
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42
)

model = Pipeline([
    ("scale",
    StandardScaler()),
    ("classifier", LogisticRegression(
        random_state=42,
        max_iter=1000
    ))
])

model.fit(X_train, y_train)
# Train the model
model.fit(X_train, y_train)
# Display training completion
print("Model training completed!")

# Create information for a new developer
new_developer = pd.DataFrame(
    [[3.5, 72, 4, 75]],
    columns=[
        "experience",
        "coding_score",
        "projects",
        "technical_score"
    ]
)

# Predict the interview result
prediction = model.predict(new_developer)
# Get the predicted probability
probability = model.predict_proba(new_developer)
# Display the prediction
if prediction[0] == 1:
    print("Prediction: Interview Pass")
else:
    print("Prediction: Interview Fail")
# Display probability for each class
print("Class probabilities:", probability)

# Generate predictions for test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
# Calculate precision
precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)
# Calculate recall
recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)
# Calculate F1-score
f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)
# Display evaluation metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
# Display detailed classification report
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))

# Create confusion matrix visualization
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)
# Draw the confusion matrix
display.plot(cmap="Blues")
# Add chart title
plt.title("Developer Interview Prediction")
# Display the visualization
plt.show()