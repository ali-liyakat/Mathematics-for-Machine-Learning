import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 10000) # start, finish, n points

y = x**2 + 2*x + 2

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-5, 10)
plt.ylim(-10, 80)
plt.axvline(x=5, color='purple', linestyle='--')
plt.axhline(y=37, color='purple', linestyle='--')
_ = ax.plot(x,y)
plt.show()

def my_fxn(my_x):
    my_y = (my_x**2 - 1)/(my_x - 1)
    return my_y

print(my_fxn(2))

# my_fxn(1)     Divide by zero error

my_fxn(0.9)
my_fxn(0.999)
my_fxn(1.1)
my_fxn(1.001)

y = my_fxn(x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.axvline(x=1, color='purple', linestyle='--')
plt.axhline(y=2, color='purple', linestyle='--')
_ = ax.plot(x,y)
plt.show()




def sin_fxn(my_x):
    my_y = np.sin(my_x)/my_x
    return my_y

# y = sin_fxn(0)

sin_fxn(0.1)
sin_fxn(0.001)
sin_fxn(-0.1)
sin_fxn(-0.001)

y = sin_fxn(x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-10, 10)
plt.ylim(-1, 2)
plt.axvline(x=0, color='purple', linestyle='--')
plt.axhline(y=1, color='purple', linestyle='--')
_ = ax.plot(x,y)
plt.show()


def inf_fxn(my_x):
    my_y = 25/my_x
    return my_y

inf_fxn(1e3)
inf_fxn(1e6)

y = inf_fxn(x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-10, 10)
plt.ylim(-300, 300)
_ = ax.plot(x, y)
plt.show()


left_x = x[x<0]
right_x = x[x>0]

left_y = inf_fxn(left_x)
right_y = inf_fxn(right_x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-10, 10)
plt.ylim(-300, 300)
ax.plot(left_x, left_y, c='C0')
_ = ax.plot(right_x, right_y, c='C0')
plt.show()