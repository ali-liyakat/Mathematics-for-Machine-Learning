# Vectors
#  -> one dimensional array of numbers
#  -> Representing a point in Space 
# -> Vectors representing magnitude and direction from origin

# Vectors (Rank 1 tensors) in Numpy
import numpy as np

x = np.array([10,5,20])
print(x)
print(x.shape)
print(type(x))
print(len(x))

print(x[0])   # zero indexed

# Vector Transposition

# Transposing regular 1D array has no effect
x_t = x.T
print(x_t)
print(x_t.shape)

# use matrix style
y = np.array([[20,30,40]])
print(y.shape)

y_t = y.T
print(y_t)
print(y_t.shape)

# we can transpose back to original shape
print(y_t.T)

# Zero vectors
#  -> Have no effect if added to other vectors

z = np.zeros(3)
print(z)

# Vectors in Pytorch and TensorFlow
import torch
import tensorflow as tf

x_pt = torch.Tensor([10,20,30])
print(x_pt)

y_pt = tf.Variable([40,50,60])
print(y_pt)