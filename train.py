import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("train.csv")

X = data[
    [
        "GrLivArea",
        "OverallQual",
        "BedroomAbvGr",
        "FullBath",
        "GarageCars"
    ]
]

y = data["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, alpha=0.6)
plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("House Price Prediction using Linear Regression")
plt.show()
