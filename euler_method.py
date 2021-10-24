# Solution to the Problem 1 Tutorial 1
# Method used: Euler's Method (First order method to solve ODE)

import numpy as np
from matplotlib import pyplot as plt

# T[n+1] = T[n] - k * (T[n] - T_a) * dt
# T[n+1] = T[n] - 0.017 * (T[n] - 21) * dt

# Parameters
k = 0.017
T_a = 21

# Variables 
t_init = 0
t_final = 10
dt = 1
T_init = 68

t_axis = [i*dt for i in range(int((t_final-t_init)/dt)+1)]
T_approx = np.zeros(np.size(t_axis))
T_analytical = np.zeros(np.size(t_axis))
T_approx[0] = T_init
T_analytical[0] = T_init

for i in range(1, len(t_axis)):
    #Compute T by the numerical method
    T_approx[i] = T_approx[i-1] - k * (T_approx[i-1] - T_a) * dt
    #Compute T as the solution arrived at by Analytical method
    T_analytical[i] = 21 + 47 * np.exp(-0.017 * t_axis[i])

print("Step size taken is: "+str(dt))
print("By the iterative (numerical) method: ")
print("The value of T (Temperature) at t = "+str(t_final)+" is: "+str(T[-1]))
print("By the analytical method: ")
print("The value of T (Temperature) at t = "+str(t_final)+" is: "+str(T_analytical[-1]))

plt.plot(t_axis,T_approx,label="Computed by Numerical method")
plt.plot(t_axis,T_analytical,label="Computed by analytical method")
plt.title("Comparing the results achieved by Analytical and Numerical methods")
plt.xlabel("Time (in min)")
plt.ylabel("Temperature (in C)")
plt.legend()
plt.show()