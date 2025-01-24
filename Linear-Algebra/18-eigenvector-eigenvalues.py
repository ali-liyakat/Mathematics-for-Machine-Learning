import numpy as np
import matplotlib.pyplot as plt
import torch

# Eigenvectors and Eigenvalues

A =np.array([[-1,4], [2,-2]])
lambdas, V = np.linalg.eig(A)

print(V)        # Matrix of eigenvectors contains as many eigenvectors as there are columns of A.
                # Each column is a separate eigenvector v


print(lambdas)     # Vector of eigenvalues with corresponding eigenvalue for each eigenvector.




# Let's confirm that A * v = Lambda * v
# For first eigenvector of A

v = V[:,0] 

lambda1 = lambdas[0]

Av = np.dot(A, v)
print(Av)

print(lambda1 * v) #


# For second eigenvector of A

v2 = V[:,1]

lambda2 = lambdas[1]

Av2 = np.dot(A, v2)
print(Av2)

print(lambda2 * v2)


def plot_vectors(vectors,colors):

    plt.figure()
    plt.axvline(x=0, color='lightgrey')
    plt.axhline(y=0, color='lightgrey')

    for i in range(len(vectors)):
        x = np.concatenate([[0,0],vectors[i]])
        plt.quiver([x[0]],[x[1]],[x[2]],[x[3]], angles ='xy', scale_units='xy', scale=1, color=colors[i],)


plot_vectors([Av, v, Av2, v2],['blue', 'lightblue', 'green', 'lightgreen'])
plt.xlim(-1,4)
plt.ylim(-3,2)
plt.show()


# Using Pytorch

A_p = torch.tensor([[-1,4], [2,-2.]])

L_complex, V_complex = torch.linalg.eig(A_p)
print(L_complex)
print(V_complex)