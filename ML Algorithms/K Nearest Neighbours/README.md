# K Nearest Neighbours Algorithm

1. It is supervised learning algorithm

2. It is used for both classification and regression

3. It is simple and intuitive , No training is required

4. All calculations happen at query time. Each query takes O(nlog(n)) time

In this algorithm, euclidian distance of query point from all other points is calculated and then sorted in increasing order. Out of first k distances, Query point belongs to label with greater number in these k distances. K should be wisely chosen.