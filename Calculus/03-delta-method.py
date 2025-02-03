import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 10000) # start, finish, n points

y = x**2 + 2*x + 2

def f(my_x):
    my_y = my_x**2 + 2*my_x + 2
    return my_y

y= f(x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
_ = ax.plot(x,y)
plt.show()

print(f(2)) # identify slope where, x=2  output, y = 10

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10) # new
_ = ax.plot(x,y)
plt.show()

# The delta method uses the difference between two points to calculate slope. To illustrate this, let's define another point, where x= 5

print(f(5)) #output, y =37

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10)
plt.scatter(5, 37, c = 'orange', zorder=3) # new
_ = ax.plot(x,y)
plt.show()

m = (37-10)/(5-2)
print(m)

b = 37-m*5
print(b)

line_y = m*x + b

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10)
plt.scatter(5, 37, c='orange', zorder=3)
plt.ylim(-5, 150) # new
plt.plot(x, line_y, c='orange') # new
_ = ax.plot(x,y)
plt.show()

print(f(2.1))

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10)
plt.scatter(2.1, 10.61, c = 'orange', zorder=3)
_ = ax.plot(x,y)
plt.show()

m = (10.61-10)/(2.1-2)
print(m)

b = 10.61-m*2.1
print(b)

line_y = m*x + b

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10)
plt.scatter(2.1, 10.61, c='orange', zorder=3)
plt.ylim(-5, 150)
plt.plot(x, line_y, c='orange', zorder=3)
_ = ax.plot(x,y)
plt.show()

delta_x = 0.000001
print(delta_x)

x1 = 2
y1 = 10

x2 = x1 + delta_x
print(x2)

y2 = f(x2)
print(y2)

m = (y2 - y1)/(x2 - x1)
print(m)


# Using the delta method, find the slope of the tangent where x = -1

x1 = -1

y1 = f(x1)
print(y1)

x2 = x1 + delta_x
print(x2)

y2 = f(x2)
print(y2)

y2 = f(x1 + delta_x)
print(y2)

m = (y2-y1)/(x2-x1)
print(m)

b = y2-m*x2
print(b)

line_y = m*x + b

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(x1, y1)
plt.scatter(x2, y2, c='orange', zorder=3)
plt.ylim(-5, 150)
plt.plot(x, line_y, c='orange', zorder=3)
_ = ax.plot(x,y)
plt.show()


def diff_demo(my_f, my_x, my_delta):
    return (my_f(my_x + my_delta) - my_f(my_x)) / my_delta

deltas = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]

for delta in deltas:
    print(diff_demo(f, 2, delta))

for delta in deltas:
    print(diff_demo(f, -1, delta))