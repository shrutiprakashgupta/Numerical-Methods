# Bisection Method
import math
import random
from matplotlib import pyplot as plt

# Estimating molar volume of ethyl alcohol

# Given: The Van der Waals equation, 
# (p + (a/v^2))*(v - b) = RT

# Parameters: 
a = 12.02
b = 0.08407
R = 0.08205 #atm L mol^{-1} K^{-1}

# To find: 
# Molar volume (v) of the ideal gas at given 
p = 2.5 #atm
T = 400 #K

# The non-linear equation formed by the given relation and conditions is as follows: 
# pV^3 + (- pb - RT)V^2 + aV - ab = 0
# General form: 
# c1 * V^3 + c2 * V^2 + c3 * V + c4 = 0

c1 = p
c2 = -1 * (p*b + R*T)
c3 = a
c4 = -1*a*b

def fun(v):
    return (c1*math.pow(v,3)+c2*math.pow(v,2)+c3*v+c4)

v = [10+i*0.05 for i in range(100)]
f = [fun(v[i]) for i in range(100)]
z = [0 for i in range(100)]

plt.plot(v,f,label="function under consideration")
plt.plot(v,z,label="x-axis")
plt.xlabel("v (in L mol-1)")
plt.ylabel("Value of the function f(v)")
plt.title("Graph of f(v) for range "+str(v[0])+" to "+str(v[-1]))

# Probable range in which solution lies is 10 to 15
# Bisection method:
# From the graph, it is clear that the sign of the function is different on a and b, although this condition is checked as well
a = 10
b = 15
c = (a+b)/2
count = 0
while ((fun(a)*fun(b) < 0)&(abs(fun(c))>0.0001)):
    #Uncomment to see the intermediate points
    #plt.plot(c,fun(c),marker="x",color="r")
    #plt.text(c,fun(c),"  -"+str(count))
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
    return (3*c1*math.pow(v,2) + 2*c2*v + c3)

a = 10
b = 15
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