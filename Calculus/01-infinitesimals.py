import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 10000) # start, finish, n points

y = x**2 + 2*x + 2

fig, ax = plt.subplots()
_ = ax.plot(x,y)
plt.show()


fig, ax = plt.subplots()
ax.set_xlim([-2, -0])
ax.set_ylim([0, 2])
_ = ax.plot(x,y)
plt.show()

fig, ax = plt.subplots()
ax.set_xlim([-1.5, -0.5])
ax.set_ylim([0.5, 1.5])
_ = ax.plot(x,y)
plt.show()

fig, ax = plt.subplots()
ax.set_xlim([-1.1, -0.9])
ax.set_ylim([0.9, 1.1])
_ = ax.plot(x,y)
plt.show()

fig, ax = plt.subplots()
ax.set_xlim([-1.01, -0.99])
ax.set_ylim([0.99, 1.01])
_ = ax.plot(x,y)
plt.show()

