# Naive Bayes

This algorithm is based on Bayes theorem.
P(A/B) = (P(B/A) * P(A))/P(B)

P(A/B) = Posterior Probability
P(B/A) = Conditional Probability of B given A (lilelihood)
P(A)   = Prior Probability
P(B)   = Normalization term

- Naive Bayes is best for text classification.

- In this, Probability of one feature is independent of other feature.
  P(x|y=1) = P(x1|y=1) *  P(x2|y=1) * P(x3|y=1) * ... P(xn|y=1)
  
- Laplace smoothing : also called Add one smoothing(done in text classification for new words not present in vocab of vectorizer)  

- Multinomial Event Model Naive Bayes : Feature vector consists of frequency of words present in documents

- Multivariate Bernoulli Naive Bayes : Feature vector is a boolean array of words present in documents

- Guassian Naive Bayes : It is used for continuous values.
  
### This code includes:

- Handling categorical data using LabelEncoder of sklearn (in Mushroom Classification)

- Mushroom classification with full implementation of naive bayes from scratch

- Guassian Naive Bayes