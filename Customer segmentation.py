import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

data_path = "your_customer_data.csv"

df = pd.read_csv(data_path)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["Recency"] = (df["InvoiceDate"].max() - df["InvoiceDate"]) / pd.to_timedelta(1, unit='D')

frequency_table = df.groupby("CustomerID").size().to_frame(name="Frequency").reset_index()
df = df.merge(frequency_table, how="left", on="CustomerID")

monetary_table = df.groupby("CustomerID")["Amount"].sum().to_frame(name="Monetary").reset_index()
df = df.merge(monetary_table, how="left", on="CustomerID")

scaler = MinMaxScaler()
df[["Recency", "Frequency", "Monetary"]] = scaler.fit_transform(df[["Recency", "Frequency", "Monetary"]])

segmentation_data = df[["Recency", "Frequency", "Monetary"]]

wcss = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(segmentation_data)
    wcss.append(kmeans.inertia_)

n_clusters = 3 #based on elbow curve

kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(segmentation_data)

df["segment_id"] = kmeans.labels_

print(df)
