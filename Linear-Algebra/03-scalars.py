# Scalars

# -> No dimensions
# -> single number
# -> denoted in lowercase, italics e.g 'x'

# Scalars (Rank 0 Tensors)
x = 20
print(x)

print(type(x))

y=5
sum = x + y
print(sum)

# Scalars in Pytorch
import torch

x_pt = torch.tensor(25)
print(x_pt)
print(x_pt.shape)

y_pt = torch.tensor(20, dtype=torch.float16)
print(y_pt)


# Scalars in Tensorflow

import tensorflow as tf

x_tf = tf.Variable(20)
print(x_tf)
print(x_tf.shape)

y_pt = tf.Variable(30, dtype=tf.float32)
print(y_pt)