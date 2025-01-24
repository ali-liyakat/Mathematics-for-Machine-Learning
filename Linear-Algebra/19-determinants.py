import numpy as np
import torch

# Determinants

X = np.array([[4,2], [-5,-3]])
print(np.linalg.det(X))

N = np.array([[-4,1],[-8,2]])
print(np.linalg.det(N))         # 0.0(Singular matrix)

A = np.array([[1,2,4],[2,-1,3],[0,5,1]])
print(np.linalg.det(A))

# Using Pytorch
Y = torch.tensor([[4,2], [-5,-3.]])
print(torch.det(Y))



# Relation b/w Determinant and Eigenvalues
# det(X) = product of all eigenvalues of X


A = np.array([[1,2,4],[2,-1,3],[0,5,1]])
print(np.linalg.det(A))


lambdas, V = np.linalg.eig(A)
print(lambdas)

prod_lambdas = np.product(lambdas)
print(prod_lambdas)