import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

raw_data = pd.read_csv("customer_train.csv")

scaler = StandardScaler()
features_scaled = scaler.fit_transform(raw_data)
data = pd.DataFrame(features_scaled, columns=raw_data.columns)

k = 4
model = KMeans(n_clusters=k, random_state=42)
data["cluster"] = model.fit_predict(data)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(data["annual_income"], data["spending_score"], c=data["cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Income vs Spending Score")

plt.subplot(1, 3, 2)
plt.scatter(data["age"], data["spending_score"], c=data["cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Income vs Spending Score")


plt.subplot(1, 3, 3)
plt.scatter(data["age"], data["spending_score"], c=data["cluster"])
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.title("Age vs Annual Income")

plt.tight_layout()
plt.show()

