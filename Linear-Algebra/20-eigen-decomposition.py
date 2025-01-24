import numpy as np
import torch

# Eigendecomposition

A = np.array([[4,2], [-5,-3]])

lambdas, V = np.linalg.eig(A)
print(V)

Vinv = np.linalg.inv(V)
print(Vinv)

Lambda = np.diag(lambdas)
print(Lambda)

# Confirm  A = V * Lambda * Vinv

result = np.dot(V, np.dot(Lambda, Vinv))
print(result)


# If A is real symmetric matrix, then
    # A = Q * Lambda * Q.T

A = np.array([[2,1], [1,2]])

lambdas, Q = np.linalg.eig(A)
print(lambdas)

Lambda = np.diag(lambdas)
print(Lambda)

print(Q)
# Confirm  A = Q * Lambda * Q.T

result = np.dot(Q, np.dot(Lambda, Q.T))
print(result)


    # Using Pytorch
    
P = torch.tensor([[25, 2, -5],[3, -2, 1],[5, 7, 4.]])

lambdas, V = torch.linalg.eig(P)
print(lambdas)

Lambda = torch.diag(lambdas)
print(Lambda)

Pinv = torch.linalg.inv(V)
print(Pinv)

result = torch.matmul(V, torch.matmul(Lambda, Pinv))
print(result)