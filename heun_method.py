import math
import numpy as np
from matplotlib import pyplot 
import time 

# General parameters 
g = 9.81                #m/s^2
cd = 0.25               #kg/m
m = 68.1                #kg
k = 40                  #N/m
gamma = 8               #kg/s
L = 30                  #m

# Computational parameters
x_0 = 0
v_0 = 0
del_t = 0.1
t = np.array([i*del_t for i in range(0,int(50/del_t)+1)])

def der_v(x,v):
    if(x>L):
        der_v_val = g - (k/m)*(x-L) - (gamma/m)*v
        if(v>0):
            der_v_val = der_v_val - (cd/m)*math.pow(v,2)
        elif(v<0):
            der_v_val = der_v_val + (cd/m)*math.pow(v,2)
    else:
        der_v_val = g       
        if(v>0):
            der_v_val = der_v_val - (cd/m)*math.pow(v,2)
        elif(v<0):
            der_v_val = der_v_val + (cd/m)*math.pow(v,2)
    return der_v_val

# Euler's method:
# Approximating derivative with the first order difference
def euler_fun_v(x,v,del_t=del_t):
    v_next = v + del_t*der_v(x,v)
    return v_next

def euler_fun_x(v,x,del_t=del_t):
    x_next = x + del_t*v
    return x_next

x = np.zeros(np.size(t))
x[0] = x_0
v = np.zeros(np.size(t))
v[0] = v_0

time_init = time.time()
for i in range(1,len(x)):
    v[i] = euler_fun_v(x[i-1],v[i-1])
    x[i] = euler_fun_x(v[i-1],x[i-1])
time_fin = time.time()

print("Solution with Euler's method: ")
print("Length at t=50s: "+str(x[-1]))
print("Velocity at t=50s: "+str(v[-1]))
print("Time taken for the execution is: "+str(time_fin-time_init))

pyplot.figure(1)
pyplot.plot(t,x,label="Variation in length with time")
pyplot.plot(t,v,label="Variation in velocity with time")
pyplot.title("Solution with the Euler's method")
pyplot.legend()
pyplot.show()
pyplot.close(1)

# Heun's method
x = np.zeros(np.size(t))
x0 = np.zeros(np.size(t))
x[0] = x_0
x0[0] = x_0

v = np.zeros(np.size(t))
v0 = np.zeros(np.size(t))
v[0] = v_0
v0[0] = v_0

time_init = time.time()
for i in range(1,len(x)):
    x0[i] = euler_fun_x(v[i-1],x[i-1])
    v0[i] = euler_fun_v(x[i-1],v[i-1])
    der_v1 = der_v(x[i-1],v[i-1])
    der_v2 = der_v(x0[i],v0[i])
    v[i] = v[i-1] + del_t*(der_v1+der_v2)/2
    der_x1 = v[i-1]
    der_x2 = v[i]
    x[i] = x[i-1] + del_t*(der_x1+der_x2)/2
time_fin = time.time()

print("Solution with Heun's method: ")
print("Length at t=50s: "+str(x[-1]))
print("Velocity at t=50s: "+str(v[-1]))
print("Time taken for the execution is: "+str(time_fin-time_init))

pyplot.figure(2)
pyplot.plot(t,x,label="Variation in length with time")
pyplot.plot(t,v,label="Variation in velocity with time")
pyplot.title("Solution with the Heun's method")
pyplot.legend()
pyplot.show()
pyplot.close(2)

# Midpoint method
x = np.zeros(np.size(t))
x0 = np.zeros(np.size(t))
x[0] = x_0
x0[0] = x_0

v = np.zeros(np.size(t))
v0 = np.zeros(np.size(t))
v[0] = v_0
v0[0] = v_0

time_init = time.time()
for i in range(1,len(x)):
    x0[i] = euler_fun_x(v[i-1],x[i-1],del_t/2)
    v0[i] = euler_fun_v(x[i-1],v[i-1],del_t/2)
    der_v_mid = der_v(x0[i],v0[i])
    v[i] = v[i-1] + del_t*der_v_mid
    x[i] = x[i-1] + del_t*v0[i]
time_fin = time.time()

print("Solution with Midpoint method: ")
print("Length at t=50s: "+str(x[-1]))
print("Velocity at t=50s: "+str(v[-1]))
print("Time taken for the execution is: "+str(time_fin-time_init))

pyplot.figure(3)
pyplot.plot(t,x,label="Variation in length with time")
pyplot.plot(t,v,label="Variation in velocity with time")
pyplot.title("Solution with the Midpoint method")
pyplot.legend()
pyplot.show()
pyplot.close(3)