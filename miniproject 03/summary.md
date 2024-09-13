### Mini-Project 3: Exploring Unsupervised Learning Techniques

### Tasks Overview

#### 1. **Clustering Algorithms Implementation**:
   - **K-Means Clustering**
   - **Hierarchical Clustering**
   - **DBSCAN**

#### 2. **Dimensionality Reduction Techniques**:
   - **Principal Component Analysis (PCA)**
   - **t-SNE (t-Distributed Stochastic Neighbor Embedding)**

#### 3. **Advanced Clustering Techniques Overview**:
   - Research advanced clustering methods beyond the basic ones mentioned.
   
#### 4. **Dimensionality Reduction Techniques Comparison**:
   - Compare PCA and t-SNE in terms of application and results.

#### 5. **Applications of Unsupervised Learning**:
   - Explore real-world applications such as anomaly detection, customer segmentation, etc.

---

### 1. **Clustering Algorithms Implementation**

#### a. **K-Means Clustering**

1. **Loading Data**: Use any high-dimensional dataset (e.g., the `Iris` dataset).

   ```python
   from sklearn.datasets import load_iris
   from sklearn.cluster import KMeans
   import matplotlib.pyplot as plt
   import numpy as np

   # Load dataset
   data = load_iris()
   X = data.data

   # Apply KMeans
   kmeans = KMeans(n_clusters=3)
   kmeans.fit(X)
   labels = kmeans.labels_
   ```

2. **Elbow Method**: Determine the optimal number of clusters.

   ```python
   wcss = []
   for i in range(1, 11):
       kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
       kmeans.fit(X)
       wcss.append(kmeans.inertia_)

   plt.plot(range(1, 11), wcss)
   plt.title('Elbow Method')
   plt.xlabel('Number of clusters')
   plt.ylabel('WCSS')
   plt.show()
   ```

3. **Silhouette Score** (Alternative for optimal clusters):

   ```python
   from sklearn.metrics import silhouette_score

   silhouette_avg = silhouette_score(X, labels)
   print(f'Silhouette Score: {silhouette_avg}')
   ```

---

#### b. **Hierarchical Clustering**

1. **Agglomerative Clustering**:

   ```python
   from sklearn.cluster import AgglomerativeClustering
   import scipy.cluster.hierarchy as sch

   # Plot dendrogram
   dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
   plt.title('Dendrogram')
   plt.xlabel('Samples')
   plt.ylabel('Distance')
   plt.show()

   # Apply Agglomerative Clustering
   hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
   y_hc = hc.fit_predict(X)
   ```

2. **Advantages & Disadvantages**:
   - **Advantages**: Doesn’t require the number of clusters to be predefined.
   - **Disadvantages**: Sensitive to noise, computationally expensive.

---

#### c. **DBSCAN (Density-Based Clustering)**

1. **Implementation**:

   ```python
   from sklearn.cluster import DBSCAN

   dbscan = DBSCAN(eps=0.5, min_samples=5)
   labels_dbscan = dbscan.fit_predict(X)
   ```

2. **DBSCAN vs. K-Means**:
   - **DBSCAN**: Suitable for datasets with noise and varying densities. It doesn't require a predefined number of clusters.
   - **K-Means**: Requires a fixed number of clusters and assumes spherical shapes for clusters.

---

### 2. **Dimensionality Reduction Techniques**

#### a. **Principal Component Analysis (PCA)**

1. **Implementation**:

   ```python
   from sklearn.decomposition import PCA

   # Apply PCA
   pca = PCA(n_components=2)
   X_pca = pca.fit_transform(X)

   # Plotting the PCA-transformed data
   plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels)
   plt.title('PCA')
   plt.xlabel('PC1')
   plt.ylabel('PC2')
   plt.show()

   # Explained variance ratio
   print(f'Explained Variance Ratio: {pca.explained_variance_ratio_}')
   ```

2. **Explanation**:
   - PCA reduces dimensions by projecting data onto the directions of maximum variance. Useful for compressing data while retaining the most significant information.

---

#### b. **t-SNE (t-Distributed Stochastic Neighbor Embedding)**

1. **Implementation**:

   ```python
   from sklearn.manifold import TSNE

   # Apply t-SNE
   tsne = TSNE(n_components=2)
   X_tsne = tsne.fit_transform(X)

   # Plotting the t-SNE-transformed data
   plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=labels)
   plt.title('t-SNE')
   plt.show()
   ```

2. **PCA vs. t-SNE**:
   - **PCA** is a linear technique, preserving global structure.
   - **t-SNE** is nonlinear and focuses on preserving local structure. It’s better for visualizing complex high-dimensional data but can distort global relationships.

---

### 3. **Advanced Clustering Techniques Overview**

One advanced clustering method is **Gaussian Mixture Models (GMM)**. Unlike K-Means, which assumes spherical clusters, GMM models data as a mixture of several Gaussian distributions, making it more flexible for clustering complex shapes.

---

### 4. **Dimensionality Reduction Techniques Comparison**

- **PCA**:
   - **Strengths**: Efficient for large datasets, preserves global structure.
   - **Weaknesses**: Linear, might not capture complex relationships.
   - **Use Case**: Preprocessing step for models sensitive to high dimensionality.

- **t-SNE**:
   - **Strengths**: Excellent for visualizing high-dimensional datasets.
   - **Weaknesses**: Computationally expensive, sensitive to parameter tuning.
   - **Use Case**: Visualizing clusters in high-dimensional data.

---

### 5. **Applications of Unsupervised Learning**

- **Customer Segmentation**: Unsupervised learning helps in dividing customers into different segments based on purchasing behavior. Techniques like K-Means or DBSCAN can identify similar groups, allowing businesses to tailor their marketing strategies.
- **Anomaly Detection**: Using clustering techniques to detect outliers, anomalies can be flagged for further investigation.
  
---

### Presentation Tips:

When preparing your presentation, include:
- Visualizations of clustering and dimensionality reduction results.
- Code snippets to show how you implemented the algorithms.
- Comparisons between techniques (e.g., PCA vs. t-SNE, K-Means vs. DBSCAN).
- Real-world application examples (e.g., customer segmentation).
