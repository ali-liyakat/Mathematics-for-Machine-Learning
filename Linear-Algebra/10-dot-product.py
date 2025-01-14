import numpy as np
import torch
import tensorflow as tf

# Dot Product

x = np.array([25, 2, 5])

y = np.array([0, 1 ,2])

print(25*0 + 2*1 + 5*2)     # Manual

print(np.dot(x, y))         # using numpy

# Using Pytorch

x_pt = torch.tensor([25, 2, 5])

y_pt = torch.tensor([0, 1, 2])

print(torch.dot(x_pt, y_pt))


# Using Tensorflow

x_tf = tf.Variable([25, 2, 5])
y_tf = tf.Variable([0, 1, 2])

print(tf.reduce_sum(tf.multiply(x_tf,y_tf)))
