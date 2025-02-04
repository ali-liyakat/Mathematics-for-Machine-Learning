# Automatic Differentiation in Pytorch
import torch

# y = x**2
# find derivative at x = 5

x = torch.tensor(5.0)
print(x)

x.requires_grad_() # contagiously track gradients through forward pass

y = x**2

y.backward() # use autodiff

print(x.grad)


# Automatic Differentiation in Tensorflow

import tensorflow as tf

x = tf.Variable(5.0)

with tf.GradientTape() as t:
    t.watch(x) # track forward pass
    y = x**2

print(t.gradient(y, x)) # use autodiff
