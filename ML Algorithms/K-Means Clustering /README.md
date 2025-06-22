## K-Means Clustering 
- It is an unsupervised learning algorithm.
- It is used to group common data together
- Common clustering technique, known as hard clustering where evry point belongs to only one cluster.
- By K-Means, it means partiion the data into k clusters.
- It fails on complex datasets.
- K-Means is special case of Expectation Maximzation Algorithm.

### K-Means Algorithm
Input Data : X = {x1,...,xN}<br>
Goal : Partition the data among some K number of clusters. Let us assume K is known to us.<br>
Let µk denote the center of Kth Cluster (uk will be vector)<br>
So we need to ﬁnd an assignment of data points to clusters, as well as a set of cluster centers{µk}, such that the sum of the squares of the distances of each data point to its closest cluster center µk, is a minimum.

### DBSCAN
- Density based Spatial Clustering of Applications with Noise
- Based upon the idea that a cluster is a high density area surrounded by low density region

### Implementation:
- [K-Means Implementation from scratch](./K-Means%20Implementation%20from%20scratch.ipynb)
- [K-Means sklearn Implementation (K-Means++)](./K-Means%20Implementation%20using%20sklearn.ipynb)
- [DBSCAN Implementation](./K-Means%20and%20DBSCAN.ipynb)
