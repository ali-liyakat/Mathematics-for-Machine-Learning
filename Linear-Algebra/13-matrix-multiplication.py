import numpy as np
import torch
import tensorflow as tf

# Matrix Multiplication with a vector

A = np.array([[3,4], [5,6],[7,8]])
B= np.array([1,2])
# print(np.dot(A, B))

# In Pytorch

A_pt = torch.tensor([[3,4], [5,6],[7,8]])
B_pt= torch.tensor([1,2])
# print(torch.matmul(A_pt, B_pt))


# In Tensorflow

A_tf = tf.Variable([[3,4], [5,6],[7,8]])
B_tf = tf.Variable([1,2])
# print(tf.linalg.matvec(A_tf, B_tf))




# Matrix by Matrix Multplication

X = np.array([[3,4], [5,6],[7,8]])
Y = np.array([[1,9], [2,0]])
print(np.dot(X, Y))


X_pt = torch.tensor([[3,4], [5,6],[7,8]])
Y_pt = torch.tensor([[1,9], [2,0]])
print(torch.matmul(X_pt, Y_pt))


X_tf = tf.Variable([[3,4], [5,6],[7,8]])
Y_tf = tf.Variable([[1,9], [2,0]])
print(tf.matmul(X_tf, Y_tf))