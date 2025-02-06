import torch
import matplotlib.pyplot as plt

x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.]) # E.g.: Dosage of drug for treating Alzheimer's disease
print(x)

# y = m*x + b    m = -0.5, b = 2
# y = -0.5*x + 2 + torch.normal(mean=torch.zeros(8), std=0.2)

# fixed example of y 
y = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37]) # E.g.: Patient's "forgetfulness score"
print(y)

fig, ax = plt.subplots()
plt.title("Clinical Trial")
plt.xlabel("Drug dosage (mL)")
plt.ylabel("Forgetfulness")
_ = ax.scatter(x, y)
plt.show()

# Initialize the slope (m) parameter with a "random" value of 0.9...
m = torch.tensor([0.9]).requires_grad_()
print(m)

# do same for b
b = torch.tensor([0.1]).requires_grad_()
print(b)

def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b

def regression_plot(my_x, my_y, my_m, my_b):
    
    fig, ax = plt.subplots()

    ax.scatter(my_x, my_y)
    
    x_min, x_max = ax.get_xlim()
    y_min = regression(x_min, my_m, my_b).detach().item()
    y_max = regression(x_max, my_m, my_b).detach().item()
    
    ax.set_xlim([x_min, x_max])
    _ = ax.plot([x_min, x_max], [y_min, y_max])

regression_plot(x, y, m, b)
plt.show()