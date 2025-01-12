# Basic Tensor Arithmetic
import numpy as np
import tensorflow as tf
import torch

X = torch.tensor([[1, 2, 3],[4, 5, 6]])
# print(X + 2)
# print(X * 2)

# print(X * 2 + 2)        # operator overloading


# Operation in Pytorch
x_pt = torch.add(torch.mul(X, 2), 2)
# print(x_pt)


# Operation in Tensorflow
x_tf = tf.add(tf.multiply(X, 2), 2)
# print(x_tf)


# Hadamard Product
Y = torch.tensor([[25, 2],[5, 26],[3, 7]])
A = Y + 2
print (A + Y)
print(A * Y)

# Hadamard Product is same in Pytorch and Tensorflow 