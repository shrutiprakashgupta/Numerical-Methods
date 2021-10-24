# Shooting method: 
# To convert boundary value problem into initial value problem  
import numpy as np
from matplotlib import pyplot as plt

# Explicit Method to solve the IVP
A = 0.1
Z = -0.16667
Z0 = Z

h = 0.1
k = 5e-6
D = 1.5e-6

L = 4
AL = 0

distr_A1 = np.zeros(int(L/h)+1)

for i in range(int(L/h)+1):
    distr_A1[i] = A
    A = A + h*Z
    Z = Z + (k*A*h)/D

print("Error: " + str(distr_A1[-1]-AL))
fig = plt.figure(1)
plt.plot(distr_A1)
plt.plot(int(L/h),AL,"o")
plt.title("With predicted Z = "+str(Z0))
plt.show()
input()

# Runge Kutta Method 
A = 0.1
Z = -0.18257
Z0 = Z
x = 0

def f(x,A,Z):
    return Z

def g(x,A,Z):
    return (k*A)/D

distr_A2 = np.zeros(int(L/h)+1)

for i in range(int(L/h)+1):
    distr_A2[i] = A
    k1 = h*f(x,A,Z)
    l1 = h*g(x,A,Z)
    k2 = h*f(x+(h/2),A+(k1/2),Z+(l1/2))
    l2 = h*g(x+(h/2),A+(k1/2),Z+(l1/2))
    k3 = h*f(x+(h/2),A+(k2/2),Z+(l2/2))
    l3 = h*g(x+(h/2),A+(k2/2),Z+(l2/2))
    k4 = h*f(x+h,A+k3,Z+l3)
    l4 = h*g(x+h,A+k3,Z+l3)
    A = A + (k1 + 2*k2 + 2*k3 + k4)/6
    Z = Z + (l1 + 2*l2 + 2*l3 + l4)/6

print("Error: " + str(distr_A2[-1]-AL))
fig = plt.figure(2)
plt.plot(distr_A2)
plt.plot(int(L/h),AL,"o")
plt.title("With predicted Z = "+str(Z0))
plt.show()