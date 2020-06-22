# Support Vector Machines

- SVM is a powerful classifier that works both on linearly and non-linearly separable data
<img src="img/linearly_separable.png" alt="Linear Separable" width="500" height="200" />

- **Goal of SVM** : Finds an optimal hyperplane, that best separates our data so that the distance from nearest points in space to itself(also called margin) is maximized

- These nearest points are called **Support Vectors**

<img src="img/svm_margin.png" alt="Support Vectors" width="300" height="300" />

- For the non-linearly separable case, it uses 'Kernel Trick'.

### What does hyperplane mean ?

<img src="img/hyperplanes.jpg" alt="Hyperplanes" width="300" height="300" />

A hyperplane is plane of _n-1_ dimensions in _n_ dimensional feature space, that separates the two classes. 
For a 2-D feature space, it would be a line and for a 3-D Feature space it would be plane and so on.

<img src="img/3d_hyperplane.png" alt="Hyperplanes" width="300" height="300" />



A hyperplane is able to separate classes if for all points -

#### **_w_ x** + b > 0 
(For data points in class 1)  
#### **_w_ x** + b < 0 
(For data points in  class 0)

### Maximum Margin Hyperplane 

An optimal hyperplane best separates our data so that the distance/margin from nearest points(called Support Vectors) in space to itself is maximized.

<img src="img/maximum_margin.png" alt="Hyperplanes" width="300" height="300" />

### SVM Implementation using Pegasos

**Formulating SVM as Unconstrainted Optimization Problem**

Paper - [Pegasos: Primal Estimated sub-GrAdient SOlver for SVM](http://www.ee.oulu.fi/research/imag/courses/Vedaldi/ShalevSiSr07.pdf)

**The final SVM Objective we derived was** -

<img src="img/loss.png" alt="Hinge Loss" width="500" height="200" />

**Gradient Descent Update Rule** -

w  = w - n*w  if ti>=1
   = w - n*w  + n*c*[yixi] if ti<1
   
b  = b if ti>=1
   = b + n*c*yi if ti<1
   
c=penalty   
n=learning_rate
w=theta
b=bias/intercept


## Non-Linear Classification
- In many real life problems, the data is not linearly separable,but we need to classify the data. This can be done using by projecting the data to higer dimesions so that it becomes linearly separable.
<img src="img/linearly_separable.png" alt="Linear Separable" width="500" height="200"/>

### Projecting data to higher dimensions!
When working with non-linear datasets, we can project orginal feature vectors into higher dimensional space where they can be linearly separated!  

#### example
Data in 2-Dimensional Space
<img src="img/circles_low.png" alt="Linear Separable" width="200" height="200"/>

Data Projected in 3-D Dimensional Space, after processing the original data using a non-linear function.
<img src="img/circles_3d.png" alt="Linear Separable" width="200" height="200"/>


## Kernel Based Classifcation in SVM's
Sklearn supports the following types of Kernels, which can be used in many-real life problems.

- Linear Kernel
- RBF Kernel
- Polynomial Kernel
- Sigmoid Kernel

**Kernel trick** is method of using a linear classifer to solve a non-linear problem. It transforms the linearly in-separable data into linearly separable one.

## Grid Search 
It is used to tune parameters of an estimator.

### This folder includes:
- SVM implementation from scratch
- SVM on non-linearly separable data with kernel Tricks
- Grid Search


    

