import math
import numpy as np
# Estimating the integral of a data set 
# with odd-numbered data points 

# Input the data set, independent and dependent variables as x and y
x = [0,2,4,6,8,10,12,14,16,18,20]
y = [0,1.8,2,4,4,6,4,3.6,3.4,2.8,0]

# Checking for the conditions to be met, for the application of Simpson's 1/3 rule 
if(len(x)%2==0):
    print("Simpson's 1/3 rule is applicable for odd numbered data point sets.")
    exit(0)

for i in range(len(x)-2):
    if((x[i+1]-x[i])!=(x[i+2]-x[i+1])):
        print("The data points are not equally spaced.")
        exit(0)

# Computing the estimated integral
# Computing the summation
integral = y[0]+y[-1]
for i in range(1,len(x)-1):
    if(i%2==0):
        integral = integral + 2*y[i]
    else:
        integral = integral + 4*y[i]

# Adding the common (b-a)/6 component
# Note: here b = x[2] and a = x[0] as each area segment is computed over three data points 
integral = integral * ((x[2]-x[0])/6)
        
print("The integral is: "+str(integral))

# Comparison with Trapezoidal estimation of integral
x = np.array(x)
y = np.array(y)

y_avg = np.array([(y[i]+y[i+1])/2 for i in range(len(y)-1)])
x_del = np.array([(x[i+1]-x[i]) for i in range(len(x)-1)])
area_del = y_avg*x_del
integral_2 = np.sum(area_del)

print("The area computed with trapezoidal rule of estimation is: "+str(integral_2))