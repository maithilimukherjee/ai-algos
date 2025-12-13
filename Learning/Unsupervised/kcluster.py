import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# simple 2d points (x, y)
data = np.array([
    [1, 2],
    [1, 4],
    [1, 0],
    [10, 2],
    [10, 4],
    [10, 0]
])

# number of clusters
k = 2

# creating kmeans model
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(data)

# get cluster labels for each point
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("cluster labels:", labels)
print("cluster centroids:", centroids)

# plot
colors = ['red', 'blue']
for i in range(len(data)):
    plt.scatter(data[i][0], data[i][1], color=colors[labels[i]])
plt.scatter(centroids[:,0], centroids[:,1], color='green', marker='x', s=200)
plt.title("simple k-means clustering")
plt.show()
