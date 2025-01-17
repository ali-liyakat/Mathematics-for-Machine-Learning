import numpy as np
import torch
import tensorflow as tf

# Matrix Inversion

X = np.array([[4,2], [-5,-3]])

X_inv = np.linalg.inv(X)
print(X_inv)

Y = np.array([4,-7])

w = np.dot(X_inv, Y)
print(w)

print(np.dot(X, w))


# In Pytorch

print(torch.inverse(torch.tensor([[4,2], [-5,-3.]])))

# In Tensorflow

print(tf.linalg.inv(tf.Variable([[4,2], [-5,-3.]])))


# Matrix Inversion where No solution

X = np.array([[4,8], [1,2]])
# X_inv = np.linalg.inv(X)      numpy.linalg.LinAlgError: Singular matrix
# print(X_inv)