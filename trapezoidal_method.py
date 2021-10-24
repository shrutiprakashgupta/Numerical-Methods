import math
import numpy as np
# Implementing Trapezoidal Method
# Independent variable matrix
x = np.array([0,2,4,5,6,7,10])

# Parameters 
mu = 0.005
Q = 1e-5
pi = 3.14
p = 1e3

# Define the Mapping
def fun_r(x):
    radius = {0:2,2:1.35,4:1.34,5:1.6,6:1.58,7:1.42,10:2}
    return radius[x]*1e-3

def fun_y(r):
    y = (-8*mu*Q)/(pi*math.pow(r,4))
    return y

# Dependent variable matrix 
r = np.array([fun_r(x[i]) for i in range(len(x))])
y = np.array([fun_y(r[i]) for i in range(len(r))])

def num_integration(x,y):
    y_avg = np.array([(y[i]+y[i+1])/2 for i in range(len(y)-1)])
    x_del = np.array([(x[i+1]-x[i]) for i in range(len(x)-1)])
    area_del = y_avg*x_del
    area = np.sum(area_del)
    return area

pressure = num_integration(x*1e-2,y)    #x is in cm
print("Pressure computed with including the effects of varying radius: "+str(pressure))

# Pressure computed with constant radius
# Computing the average radius 

r_mean = num_integration(x,r)/(x[-1]-x[0])  #cm gets cancelled out
print("Average radius is: "+str(r_mean))
pressure_avg = fun_y(r_mean)*((x[-1]-x[0])*1e-2)
print("Pressure computed with assumed average radius: "+str(pressure_avg))

def fun_Re(r):
    Re_num = (2*p*Q)/(pi*mu*r)
    return Re_num

Re = [fun_Re(r[i]) for i in range(len(r))]
Re_mean = num_integration(x,Re)/(x[-1]-x[0])
print("Average Reynold's number is: "+str(Re_mean))