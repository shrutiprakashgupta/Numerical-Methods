# Computation of Value using Truncated Taylor Series Method
import math

# Target and the base points
base = 1
target = 3

# Nth order derivatives 
def dev_0 (x):
    f_0 = 25 * math.pow(x,3) - 6 * math.pow(x,2) + 7 * math.pow(x,1) - 88
    return f_0

def dev_1 (x):
    f_1 = 75 * math.pow(x,2) - 12 * math.pow(x,1) + 7
    return f_1

def dev_2 (x):
    f_2 = 150 * math.pow(x,1) - 12
    return f_2

def dev_3 (x):
    f_3 = 150
    return f_3

# Exact value
val = dev_0(target)
# Zero order truncation 
val_0 = dev_0(base)
# First order truncation
val_1 = val_0 + (dev_1(base) * (target-base))/1
# Second order truncation
val_2 = val_1 + (dev_2(base) * math.pow((target-base),2))/2
# Third order truncation
val_3 = val_2 + (dev_3(base) * math.pow((target-base),3))/6

print("The exact value is: "+ str(val))
print("The value computed with zero order truncated Taylor series is: "+str(val_0))
print("The value computed with first order truncated Taylor series is: "+str(val_1))
print("The value computed with second order truncated Taylor series is: "+str(val_2))
print("The value computed with third order truncated Taylor series is: "+str(val_3))

def per_error (true_val, apprx_val):
    error_val = abs((true_val - apprx_val)/true_val) * 100
    return round(error_val,2)

# Error value computation 
print("The True percentage relative error with zero order truncated Taylor series is: "+str(per_error(val, val_0)))
print("The True percentage relative error with first order truncated Taylor series is: "+str(per_error(val, val_1)))
print("The True percentage relative error with second order truncated Taylor series is: "+str(per_error(val, val_2)))
print("The True percentage relative error with third order truncated Taylor series is: "+str(per_error(val, val_3)))
