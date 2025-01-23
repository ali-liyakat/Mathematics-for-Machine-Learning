import numpy as np
import matplotlib.pyplot as plt

''' AFFINE TRANSFORMATIONS
        1:- Flipping
        2:- Rotation
        3:- Scaling
        4:- Shearing
        '''


v =np.array([3, 1])

def plot_vectors(vectors,colors):

    plt.figure()
    plt.axvline(x=0, color='lightgrey')
    plt.axhline(y=0, color='lightgrey')

    for i in range(len(vectors)):
        x = np.concatenate([[0,0],vectors[i]])
        plt.quiver([x[0]],[x[1]],[x[2]],[x[3]], angles ='xy', scale_units='xy', scale=1, color=colors[i],)

plot_vectors([v],['lightblue'])
plt.xlim(-1,5)
plt.ylim(-1,5)
plt.show()          # Displays the v vector


I = np.array([[1,0],[0,1]])

Iv =np.dot(I, v)

plot_vectors([Iv],['blue'])
plt.xlim(-1,5)
plt.ylim(-1,5)
plt.show()          # displays the Iv vector(vecor v multiplied by identity vector I) No change


E = np.array([[1,0],[0,-1]])
Ev = np.dot(E, v)
plot_vectors([v, Ev],['lightblue', 'blue'])
plt.xlim(-1,5)
plt.ylim(-3,3)
plt.show()          # Rotates the vector v by x axis


F = np.array([[-1,0],[0,1]])
Fv =np.dot(F,v)
plot_vectors([v, Fv],['lightblue', 'blue'])
plt.xlim(-4,4)
plt.ylim(-1,5)
plt.show()          # Rotates vector v by y axis


A = np.array([[-1,4],[2,-2]])
Av =np.dot(A,v)
plot_vectors([v, Av],['lightblue', 'blue'])
plt.xlim(-1,5)
plt.ylim(-1,5)
plt.show()          # Rotates by some angle

v2 = np.array([2,1])
plot_vectors([v2, np.dot(A, v2)], ['lightgreen', 'green'])
plt.xlim(-1,5)
plt.ylim(-1,5)
plt.show()      # Rotated by small angle
