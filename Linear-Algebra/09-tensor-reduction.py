import torch
import tensorflow as tf

# Tensor Reduction

X = torch.tensor([[25, 2],[5, 26],[3, 7]])
# print(X.sum())

# print(torch.sum(X))

# print(tf.reduce_sum(X))

print(X.sum(axis=0))    # Summing all columns
print(X.sum(axis=1))    # Summing all rows

print(torch.sum(X, 0))
print(tf.reduce_sum(X, 1))


print(torch.max(X))

# Other operations are
    # -> Minimum
    # -> Mean
    # -> Product