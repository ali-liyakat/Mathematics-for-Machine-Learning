import numpy as np

# Moore-Penrose Pseudoinverse

A = np.array([[-1,2], [3, -2], [5,7]])

U, d, VT = np.linalg.svd(A)
print(U)
print(VT)
print(d)

D = np.diag(d)
print(D)


# This takes the reciprocal of Non-zero elements.
Dinv = np.linalg.inv(D)
print(Dinv)


# D+ must have same dimesions as A+
DPlus = np.concatenate((Dinv, np.array([[0,0]]).T), axis=1)
print(DPlus)

res = np.dot(VT.T, np.dot(DPlus, U.T))
print(res)


# Numpy ,ethod for Pseudoinverse
print(np.linalg.pinv(A))

# Using Pytorch
import torch

A_p = torch.tensor([[-1,2],[3,-2],[5,7.]])
print(torch.pinverse(A_p))
