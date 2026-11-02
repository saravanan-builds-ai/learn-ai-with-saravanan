import joblib

model = joblib.load('model/linear_regression.pkl')

result =model.predict([[10]])

print(result[0])
