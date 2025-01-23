import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LinearRegression

train_data = pd.read_csv("salary_train.csv")
test_data = pd.read_csv("salary_test.csv")

# print(train_data.head())

X_train = train_data.drop("salary", axis=1)
y_train = train_data["salary"]

X_test = test_data.drop("salary", axis=1)
y_test = test_data["salary"]

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(50, 50))
plt.scatter(X_test["years_of_experience"], y_test)

plt.plot(X_test["years_of_experience"], y_pred, color="red")

plt.title("Regression - Nuage de point")
plt.show()
