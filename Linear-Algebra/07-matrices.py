# Matrices (Rank 2 Tensors)

import numpy as np

X = np.array([[25, 2], [10,5], [30,6]])
print(X)
print(X.shape)
print(X.size)

print(X[:, 0])      #slicing

# Matrices in Pytorch
import torch

X_pt = torch.tensor([[10, 2], [20, 4], [30, 6]])
print(X_pt)
print(X_pt.shape)


# Matrices in Tensorflow

import tensorflow as tf

X_tf = tf.Variable([[10, 2], [20, 4], [30, 6]])
print(X_tf)
print(X_tf.shape)
print(tf.shape(X_tf))
print(tf.rank(X_tf))