## Support Vector Machines

- SVM is a powerful classifier that works both on linearly and non-linearly separable data
<img src="img/linearly_separable.png" alt="Linear Separable" style="width: 200px;height:100px;"/>

- Finds an optimal hyperplane, that best separates our data so that the distance from nearest points in space to itself(also called margin) is maximized
- These nearest points are called **Support Vectors**

<img src="img/svm_margin.png" alt="Support Vectors" style="width: 100px;height:100px;"/>

- For the non-linearly separable case, it uses 'Kernel Trick'.

### What does hyperplane mean ?

<img src="img/hyperplanes.jpg" alt="Hyperplanes" style="width: 100px;height: 100px;"/>

A hyperplane is plane of _n-1_ dimensions in _n_ dimensional feature space, that separates the two classes. 
For a 2-D feature space, it would be a line and for a 3-D Feature space it would be plane and so on.

<img src="img/3d_hyperplane.png" alt="Hyperplanes" style="width: 100px; height:100px;"/>



A hyperplane is able to separate classes if for all points -

#### **_w_ x** + b > 0 
(For data points in class 1)  
#### **_w_ x** + b < 0 
(For data points in  class 0)

### Maximum Margin Hyperplane 

An optimal hyperplane best separates our data so that the distance/margin from nearest points(called Support Vectors) in space to itself is maximized.

<img src="img/maximum_margin.png" alt="Hyperplanes" style="width: 400px;"/>

### SVM Implementation using Pegasos

**Formulating SVM as Unconstrainted Optimization Problem**

Paper - [Pegasos: Primal Estimated sub-GrAdient SOlver for SVM](http://www.ee.oulu.fi/research/imag/courses/Vedaldi/ShalevSiSr07.pdf)

The final SVM Objective we derived was -

<img src="img/loss.png" alt="Hinge Loss" style="width: 400px;"/>



