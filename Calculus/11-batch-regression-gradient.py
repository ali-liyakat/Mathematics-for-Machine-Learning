import torch
import matplotlib.pyplot as plt

xs = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.])
ys = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37])

def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b

m = torch.tensor([0.9]).requires_grad_()
b = torch.tensor([0.1]).requires_grad_()

# Step 1: Forward pass
yhats = regression(xs, m, b)
print(yhats)

# Step 2: compare y^ with true y to calculate cost C
# Mean Squared Error  C =1/nSumm(y^ -y)**2

def mse(my_yhat, my_y): 
    sigma = torch.sum((my_yhat - my_y)**2)
    return sigma/len(my_y)

C = mse(yhats, ys)
print(C)

# Step 3: Use autodiff to calculate gradient of C w.r.t. parameters

C.backward()
print(m.grad)
print(b.grad)

# Gradient of Mean squared error
#dC/dm = 2/nSumm(y^ -y)*x
print(2*1/len(ys)*torch.sum((yhats - ys)*xs))

#dC/db = 2/nSumm(y^ -y)
print(2*1/len(ys)*torch.sum(yhats - ys))

gradient = torch.tensor([[b.grad.item(), m.grad.item()]]).T
print(gradient)