import numpy as np
import torch

# Symmetric Matrix

X_sym = np.array([[0,1,2],[1,7,8],[2,8,9]])
print(X_sym)


X_symT = X_sym.T
print(X_symT)

print(X_sym == X_symT)


# Identity Matrix

I = torch.tensor([[1,0,0], [0,1,0], [0,0,1]])
print(I)

x_pt = torch.tensor([20,5,4])
print(torch.matmul(x_pt, I))