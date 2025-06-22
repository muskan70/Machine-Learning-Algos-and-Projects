## Naive Bayes
This algorithm is based on Bayes theorem.<br>
P(A/B) = (P(B/A) * P(A))/P(B)<br>
P(A/B) = Posterior Probability<br>
P(B/A) = Conditional Probability of B given A (lilelihood)<br>
P(A)   = Prior Probability<br>
P(B)   = Normalization term<br>

- Naive Bayes is best for text classification.
- In this, Probability of one feature is independent of other feature.
> P(x|y=1) = P(x1|y=1) *  P(x2|y=1) * P(x3|y=1) * ... P(xn|y=1)
- Laplace smoothing : also called Add one smoothing(done in text classification for new words not present in vocab of vectorizer)  
- Multinomial Event Model Naive Bayes : Feature vector consists of frequency of words present in documents
- Multivariate Bernoulli Naive Bayes : Feature vector is a boolean array of words present in documents
- Guassian Naive Bayes : It is used for continuous values.
  
### Implementation:
- Handling categorical data using LabelEncoder of sklearn (in Mushroom Classification)
- [Mushroom classification with full implementation of naive bayes from scratch](./Mushroom%20Classifier%20Naive%20Bayes%20Implementation.ipynb)
- [Guassian Naive Bayes](./Gaussian%20Naive%20Bayes%20using%20sklearn.ipynb)
- [Textual Data Cleaning](./Textual%20Data%20Cleaning.ipynb)
- [Textual Data Cleaning II - Working with Files](./TextualDataCleaningWorkingWithFiles.py)
- [Text Classification using Multinomial naive bayes and Bernoulli naive bayes](./Text%20Classification%20using%20MultinomialNB%20and%20BernoulliNB.ipynb)
