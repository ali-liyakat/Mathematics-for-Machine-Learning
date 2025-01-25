import numpy as np

# Trace Operator

A = np.array([[25, 2],[5, 4]])
print(A)

Tr = np.trace(A)
print(Tr)


# Confirm Tr(A) = Tr(A.T)

AT = A.T
print(AT)

print(np.trace(AT))


Af = np.linalg.norm(A)
print(Af)

# Confirm ||A||f = Squareroot(Tr(A*A.T))

For_val = np.trace(np.dot(A, AT))** (1/2)
print(For_val)

# Using Pytorch
import torch

A_p = torch.tensor([[4.0, 2.0, 1.0],[1.0, 3.0, 0.0],[2.0, 0.0, 5.0]])
print(A_p)
trace_A = torch.trace(A_p)
print(trace_A)
