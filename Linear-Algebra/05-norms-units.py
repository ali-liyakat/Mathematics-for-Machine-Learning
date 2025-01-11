# Norms
# -> Norms are functions that quantify vector magnitude
# Most common form is L^2 form
        # ||X||2 = square_root(Summation(xi^2))
        
import numpy as np

# L2 Norm

x = np.array([25, 2, 5])
print(x)
print((25**2 + 2**2 + 5**2) **(1/2))

print(np.linalg.norm(x))  # Linear Algebra module


# L1 Norm
        # -> ||X||1 = Summation(|xi|)

x = np.array([10,5,4])
print(np.abs(10) + np.abs(5) + np.abs(4))


# Squared L2 Norm
        # ||X||2^2 = Summation(xi^2)
x = np.array([25, 2, 5])
print(25**2 + 2**2 + 5**2)


# Max Norm
x = np.array([25, 2, 5])
print(np.max([np.abs(25), np.abs(2), np.abs(5)]))

# Unit Vectors
# -> special case of vectors where its length is equal to one.
# Technically X is a unit vector with "unit norm" i.e: ||X|| = 1
