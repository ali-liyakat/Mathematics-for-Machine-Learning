import numpy as np

# Singular Value Decomposition
    # ->  A = U * D * V.T

A = np.array([[-1,2], [3, -2], [5,7]])

U, d, Vt = np.linalg.svd(A)

print(U)
print(d)
print(Vt)

D = np.concatenate((np.diag(d), [[0,0]]), axis=0)   # D must have same dimesnions as A
 
res = np.dot(U, np.dot(D, Vt))
print(res)


'''
SVD and Eigendecomposition are closely related to each other:
    Left-Singular vectors of A = eigenvectors of A*A.T
    Right-Singular vectors of A = eigenvectors of A.T*A
    No-zero singular values of A = squareroots of eigenvectors of A*A.T = squareroots of eigenvectors of A of A.T*A.
    '''


# Using Pytorch

import torch

B = torch.tensor([[25, 2, -5],[3, -2, 1],[5, 7, 4.]])

U, d, VT = torch.linalg.svd(B)

print(U)
print(VT)
print(d)

d_diag = torch.diag(d)

result = torch.matmul(U, torch.matmul(d_diag, VT))
print(result)