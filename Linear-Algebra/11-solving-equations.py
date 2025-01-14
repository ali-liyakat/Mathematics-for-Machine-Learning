import numpy as np
import matplotlib.pyplot as plt


#  y = 3x  --1
#  -5x + 2y = 2  --2    => 2y = 2+ 5x  => y = (2 + 5x)/2  => y = 1 + 5x/2

x = np.linspace(-10, 10, 1000)

y1 = 3 * x
y2 = 1 + (5*x)/2

fig,ax = plt.subplots()
plt.xlabel("X")
plt.ylabel("Y")
ax.set_xlim([0, 3])
ax.set_ylim([0,8])
ax.plot(x,y1,c="green")
ax.plot(x,y2,c="brown")
plt.show()