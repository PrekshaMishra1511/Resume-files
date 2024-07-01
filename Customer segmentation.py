import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data_path = "your_customer_data.csv"
df = pd.read_csv(data_path)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Recency"] = (df["InvoiceDate"].max() - df["InvoiceDate"]).dt.days

frequency_table = df.groupby("CustomerID").size().to_frame(name="Frequency").reset_index()
monetary_table = df.groupby("CustomerID")["Amount"].sum().to_frame(name="Monetary").reset_index()

df = df.merge(frequency_table, how="left", on="CustomerID")
df = df.merge(monetary_table, how="left", on="CustomerID")

segmentation_data = df[["CustomerID", "Recency", "Frequency", "Monetary"]].drop_duplicates()

scaler = MinMaxScaler()
segmentation_data[["Recency", "Frequency", "Monetary"]] = scaler.fit_transform(segmentation_data[["Recency", "Frequency", "Monetary"]])

wcss = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(segmentation_data[["Recency", "Frequency", "Monetary"]])
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 10), wcss, marker='o', linestyle='--')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method to Determine Optimal Number of Clusters')
plt.show()

n_clusters = 3 #based on elbow curve

kmeans = KMeans(n_clusters=n_clusters, random_state=42)
segmentation_data["segment_id"] = kmeans.fit_predict(segmentation_data[["Recency", "Frequency", "Monetary"]])

df = df.merge(segmentation_data[["CustomerID", "segment_id"]], on="CustomerID", how="left")

print(df.head())
