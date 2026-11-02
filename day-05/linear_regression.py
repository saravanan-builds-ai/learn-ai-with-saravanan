# Import the LinearRegression algorithm
from sklearn.linear_model import LinearRegression

import joblib

# Import train_test_split to divide our dataset
from sklearn.model_selection import train_test_split

# Import mean_absolute_error to evaluate predictions
from sklearn.metrics import mean_absolute_error

# Input data: years of developer experience
# Each nested list represents one developer
X = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
]

# Expected salary in lakhs per year
# Each salary corresponds to the experience above
y = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# Split the data into training and testing sets
# 20% of the data is reserved for testing
# random_state ensures repeatable results
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create a Linear Regression model

model = LinearRegression()

# Train the model using training data
model.fit(X_train, y_train)

# Predict salaries for the test dataset
predictions = model.predict(X_test)

joblib.dump(model, 'model/linear_regression.pkl')

# Calculate the average absolute prediction error
mae= mean_absolute_error(y_test, predictions)
# Print actual and predicted salaries
print("Actual salaries:", y_test)
print("Predicted salaries:", predictions)

# Print model evaluation result
print("Mean Absolute Error:", mae)

# Predict salary for a developer with 6 years experience
new_developer = [[6]]

predicted_salary = model.predict(new_developer)

print(
    "Predicted salary for 6 years experience:",
    predicted_salary[0],
    "LPA"
)
mae= mean_absolute_error(new_developer, predicted_salary)
# Predict salary for a developer with 6 years experience
new_developer = [[13]]
predicted_salary = model.predict(new_developer)

print(
    "Predicted salary for 13 years experience:",
    predicted_salary[0],
    "LPA"
)
# Print model evaluation result
print("Mean Absolute Error:", mae)
# Display what the model learned
print("Slope:", round(model.coef_[0],2))
print("Intercept:", round(model.intercept_,2))

