import numpy as np

# Applying Matrices

U = np.array([2,5,-3])

V = np.array([0,-4,6])

B = np.array([[2,0,-1], [-2,3,-1], [0,4,-1]])

I = np.array([[1,0,0],[0,1,0],[0,0,1]])


# Apply identity matrix I3 to vector U.

print(np.dot(U, I))

# Apply matrix B to vector U
print(np.dot(B, U))

# Conacatenate vector U with vector V to form matrix Z, then apply matrix B to matrix Z.
Z = U + V
print(Z)
print(np.dot(Z, B))