import torch
import math

# Volume of cylinder v= pi*r^2*l
# partial derivative w.r.t l = pi*r^2

def cylinder_vol(my_r, my_l):
    return math.pi * my_r**2 * my_l

# Let's say the radius is 3 meters...
r = torch.tensor(3.).requires_grad_()
print(r)

# ...and length is 5 meters:
l = torch.tensor(5.).requires_grad_()
print(l)

# Then the volume of the cylinder is 141.4 cubic meters: 
v = cylinder_vol(r, l)
print(v)

v.backward()

print(l.grad)

# Now manual derivation 
print(math.pi * 3**2)

# Partial derivative w.r.t r = 2*pi*r*l

print(r.grad)

# Manually 
print(2 * math.pi * 3 * 5)