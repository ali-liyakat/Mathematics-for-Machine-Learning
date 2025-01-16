import numpy as np
import torch
import tensorflow as tf

# Forbenius Norm

x = np.array([[1, 2],[3, 4]])

print((1**2 + 2**2 + 3**2 + 4**2) **(1/2))      # Normal calculation

print(np.linalg.norm(x))

# Pytorch

x_pt = torch.tensor([[1, 2],[3, 4.]])   # torch.norm() requires float type
print(torch.norm(x_pt))

# Tensorflow

x_tf =tf.Variable([[1, 2],[3, 4.]])     # tf.norm() requires float type
print(tf.norm(x_tf))