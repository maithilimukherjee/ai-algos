import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# sample spending data: [groceries, entertainment]
data = np.array([
    [200, 50],
    [220, 60],
    [210, 55],
    [800, 300],  # big spender, outlier
    [205, 65],
    [50, 5],     # very low spender, outlier
    [215, 50],
    [190, 45]
])

# create DBSCAN model
# eps = maximum distance to consider neighbors
# min_samples = minimum points to form a cluster
dbscan = DBSCAN(eps=30, min_samples=2)
labels = dbscan.fit_predict(data)

print("cluster labels:", labels)

# plot clusters
unique_labels = set(labels)
colors = ['red', 'blue', 'green', 'purple', 'orange']

for k in unique_labels:
    class_member_mask = (labels == k)
    xy = data[class_member_mask]
    if k == -1:
        # noise/outliers
        plt.scatter(xy[:,0], xy[:,1], c='black', marker='x', s=100, label='outlier')
    else:
        plt.scatter(xy[:,0], xy[:,1], c=colors[k % len(colors)], s=100, label=f'cluster {k}')

plt.xlabel("Groceries Spending")
plt.ylabel("Entertainment Spending")
plt.title("DBSCAN on Spending Habits")
plt.legend()
plt.show()
