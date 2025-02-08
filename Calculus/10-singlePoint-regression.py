import torch

xs = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.])

ys = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37])

# slope y = m * x + b

def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b


# Initialize m and b with some random values
m = torch.tensor([0.9]).requires_grad_()
b = torch.tensor([0.1]).requires_grad_()

i = 7
x = xs[i]
y = ys[i]

print(x)
print(y)

# Step 1: Forward pass
yhat = regression(x, m, b)
print(yhat)

# Step 2: Compare y^ with true y to calculate cost C  C= (y^ - y)**2

def squared_error(my_yhat, my_y):
    return (my_yhat - my_y)**2

C = squared_error(yhat, y)
print(C)


# Step 3: Use autodiff to calculate gradient of C w.r.t. parameters

C.backward()

# partial derivative of C w.r.t m
print(m.grad)

# partual derivative of C w.r.t b
print(b.grad)


# Quadratic cost w.r.t predicted y

# dC/dm = 2x(y^ -y)
print(2*x*(yhat.item()-y))

# dC/db = 2(y^ -y)
print(2*(yhat.item()-y))



# The Gradient of Cost nabla C
# nabla C = [dC/db, dC/dm].T

gradient = torch.tensor([[b.grad.item(), m.grad.item()]]).T
print(gradient)

