import math
import random
from matplotlib import pyplot as plt

# Determining the amount (number of moles) of the product

#Parameters
ca0 = 42
cb0 = 28
cc0 = 4
k = 0.016  

#Coefficients of the non-linear equation 
c1 = 4*k
c2 = -4*k*(2*cb0+ca0)
c3 = k*((ca0*ca0)+4*(cb0*cb0)+8*(ca0*cb0))
c4 = (-2*k*(ca0*ca0)*(cb0*cb0))+(-4*k*ca0*(cb0*cb0))-1
c5 = k*(ca0*ca0)*(cb0*cb0) - cc0 

# The non-linear equation formed by the given relation and conditions is as follows: 
# In General form: 
# c1 * x^4 + c2 * x^3 + c3 * x^2 + c4 * x + c5 = 0
# Where, the coefficients are calculated as above mentioned

def fun(x):
    return (c1*math.pow(x,4)+c2*math.pow(x,3)+c3*math.pow(x,2)+c4*x+c5)

v = [i*0.02 for i in range(100)]
f = [fun(v[i]) for i in range(100)]
z = [0 for i in range(100)]

plt.plot(v,f,label="function under consideration")
plt.plot(v,z,label="x-axis")
plt.xlabel("x (in mol)")
plt.ylabel("Value of the function f(x)")
plt.title("Graph of f(x) for range "+str(v[0])+" to "+str(v[-1]))

# Probable range in which solution lies is 0 to 2
# Bisection method:
# From the graph, it is clear that the sign of the function is different on a and b, although this condition is checked as well
a = 0
b = 2
c = (a+b)/2
count = 0
while ((fun(a)*fun(b) < 0)&(abs(fun(c))>0.0001)):
    #Uncomment to see the intermediate points
    plt.plot(c,fun(c),marker="x",color="r")
    plt.text(c,fun(c),"  -"+str(count))
    count = count+1
    #The end point shifted accordingly
    if((fun(a)*fun(c))<0):
        b = c
    elif(fun(c)==0):
        break
    else:
        a = c
    c = (a+b)/2

print("The solution computed by Bisection method is: "+str(c))
print("The value of the function at this point is: "+str(fun(c)))
print("The number of iterations used is: "+str(count))
plt.plot(c,fun(c),marker="o",color="m",label="Bisection method")

# Newton Ramphson Method
# First derivative of the function (f(x) = 0)  
def d_fun(v):
    return (4*c1*math.pow(x,3)+3*c2*math.pow(x,2)+2*c3*x+c4)

a = 0
b = 2
random.seed(1)
# to keep the initial random value constant, so that the number of iterations depends on the error tolerance level only
x = a + random.random()*(b-a)

count = 0
while (abs(fun(x))>0.0001):
    #Uncomment to see the intermediate points
    #plt.plot(x,fun(x),marker="x",color="r")
    #plt.text(x,fun(x),"  +"+str(count))
    count = count + 1
    x = x - fun(x)/d_fun(x)

print("The solution computed by Newton Ramphson method is: "+str(x))
print("The value of the function at this point is: "+str(fun(x)))
print("The number of iterations used is: "+str(count))
plt.plot(x,fun(x),marker="o",color="g",label="Newton Raphson Method")
plt.legend()
plt.show()