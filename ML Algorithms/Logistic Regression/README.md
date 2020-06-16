# Logistic Regression

-It is a supervised learning algorithm.

-It is used for classification of data using gradient descent algorithm.

-Applicable only for linear boundary separation

### Error : Maximum of Log likelihood of theta = >

LL(theta) = sum from i=1 to m(Yi*log(h(Xi)) + (1-Yi)*log(1-h(Xi)))

### Update Rule = >

let there are m samples, k features :

i=ith sample out of 1 to m

j=jth feature out of 1 to k

theta(j) = theta(j) + (learning_rate)*(sum from i=1 to m(Yi -Ho(Xi)*Xij)
