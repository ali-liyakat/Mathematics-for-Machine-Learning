import numpy as np

# Orthogonal Vectors
    # -> Dot Product is equal to 0
    # -> Are at 90 degree angle to each other.
x = np.array([1, 0])

y = np.array([0, 1])
print(np.dot(x, y))       #0: indicates orthogonal

x_t = x.T

print(x_t*y)