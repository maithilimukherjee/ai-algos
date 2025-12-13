import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# --- 1. Create a Synthetic Dataset ---
print("### 1. Initial Data Sample ###")

# Generate mock data for 50 students
np.random.seed(42) # for reproducible results
data = {
    'GPA': np.concatenate([
        np.random.uniform(3.5, 4.0, 15), # High Achievers
        np.random.uniform(2.5, 3.5, 20), # Average
        np.random.uniform(1.5, 2.5, 15)  # Needs Improvement
    ]),
    'Study_Hours_Per_Week': np.concatenate([
        np.random.randint(15, 30, 15),
        np.random.randint(5, 15, 20),
        np.random.randint(1, 10, 15)
    ]),
    'Attendance_Pct': np.concatenate([
        np.random.randint(90, 100, 15),
        np.random.randint(70, 90, 20),
        np.random.randint(50, 75, 15)
    ])
}

df = pd.DataFrame(data)
df['Student_ID'] = [f'S{i+1}' for i in range(len(df))]
df = df.round(2)
print(df.head())
print("-" * 40)


# --- 2. Data Pre-processing (Scaling) ---
# K-Means is sensitive to the scale of features, so we normalize them.
features = ['GPA', 'Study_Hours_Per_Week', 'Attendance_Pct']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n### 2. Scaled Data Sample (First 5 Rows) ###")
print(pd.DataFrame(X_scaled, columns=features).head())
print("-" * 40)


# --- 3. Determine Optimal Number of Clusters (Elbow Method) ---
# The optimal 'k' is where the decrease in WCSS (Inertia) slows down significantly.
wcss = []
k_range = range(1, 11)

for k in k_range:
    # Initialize KMeans model
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10, max_iter=300)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plotting the Elbow Method
plt.figure(figsize=(8, 5))
plt.plot(k_range, wcss, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Within-Cluster Sum of Squares (WCSS/Inertia)')
plt.grid(True)
plt.show()

# Based on the plot, we'll assume k=3 is the optimal number of clusters for this data.
optimal_k = 3
print(f"\nOptimal K selected: {optimal_k}")
print("-" * 40)


# --- 4. Apply K-Means Clustering ---
kmeans_model = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Cluster'] = kmeans_model.fit_predict(X_scaled)


# --- 5. Analysis of Cluster Results ---
print("\n### 5. Cluster Analysis: Mean of Features by Cluster ###")
cluster_summary = df.groupby('Cluster')[features].mean().round(2)
print(cluster_summary)
print("\nInterpretation of Clusters:")
print("Cluster 0: Likely 'Needs Improvement' (Lowest GPA, Study Hours, and Attendance)")
print("Cluster 1: Likely 'High Achievers' (Highest GPA, Study Hours, and Attendance)")
print("Cluster 2: Likely 'Average' (Middle-range metrics)")
print("-" * 40)

print("\n### Students with their assigned clusters (First 10) ###")
print(df[['Student_ID', 'GPA', 'Cluster']].head(10))