## Decision Trees
- Simple Tree like structure, model makes a decision at every node
- Useful in simple tasks
- One of the most popular algorithm
- Easy explainability, easy to show how a decision process works!

### Why decision trees are popular?
- Easy to interpret and present
- Well defined Logic, mimic human level thought
- Random Forests, Ensembles of decision trees are more powerful classifiers
- Feature values are preferred to be **categorical**. If the values are continuous then they are discretized prior to building the model.

##  Build Decision Trees
Two common algorithms - 
- CART (Classification and Regression Trees) → uses Gini Index(Classification) as metric.
- ID3 (Iterative Dichotomiser 3) → uses Entropy function and Information gain as metrics

**Entropy**: It measures randomness of the system.
- Entropy = H(S) = - sum of classes(Pc * (log Pc))
  Pc=Probability of class
  
**Information Gain** : Reduction in entropy
- When a set(S) is divided into subsets:
    IG(S,A) = H(S) - sum of subsets((Sv/S) * H(Sv))
    
## Random Forests
- Problems with Decision Trees: Overfitting and High Variance
- To overcome this, Instead of making one tree make several trees - forest of trees : random forest
- It is a type of ensembling technique (Train on many weak models, then take average of all)
- Each tree can have any no.of features, different features, variations in training data means different structures.

[Implementation](./Decision%20Tree%20and%20Random%20Forest%20Implementation.ipynb)
