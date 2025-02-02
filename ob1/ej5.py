# -*- coding: utf-8 -*-
"""LassoCVXPY.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/jabazer/tao-fing/blob/master/LassoCVXPY.ipynb

Sea el problema no diferenciable sin restricciones

\begin{align}
(QP) \min_{\mathbf x \in R^{n},\mathbf t \in R^{n}} & \frac{1}{2}\|\mathbf{A}\vec{x} -\vec{b} \|^2  + \sum_{i=1}^n t_i\\
 \textrm{sujeto a: } x_i& \leq t_i \\
 -x_i&\leq t_i 
\end{align}
"""

# Import packages.
import cvxpy as cp
import numpy as np

A=np.array([[-4.100000000000000000e+01, 2.000000000000000000e+01],
[-4.600000000000000000e+01, -8.000000000000000000e+00],
[-5.000000000000000000e+00, -3.300000000000000000e+01],
[-5.500000000000000000e+01, 1.000000000000000000e+00],
[-5.500000000000000000e+01, -6.000000000000000000e+00]])

b=[8.000000000000000000e+00 , 5.000000000000000000e+00, -3.000000000000000000e+00, 1.000000000000000000e+01, 4.000000000000000000e+00]

ele=1
print(A)


x=cp.Variable(2)
t=cp.Variable(2)  
cost=0.5*cp.sum_squares(A*x-b)+ele*cp.sum(t)
constraints =[t>=x, t>=-x]
prob = cp.Problem(cp.Minimize(cost),constraints)
prob.solve()

print("El costo óptimo es", prob.value)
print("La variable x óptima es, %s" %x.value)
print("La variable t óptima es, %s" %t.value)