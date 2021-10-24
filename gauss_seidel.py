# Implementing Gauss Seidel Method
import numpy as np

# Start with the assumed value 
t11 = 0
t12 = 0
t21 = 0
t22 = 0

# Iteratively computing the values of the variables
for i in range(15):
    t12 = (225 + t22 + t11)/4
    t22 = (25 + t12 + t21)/4
    t21 = (75 + t22 + t11)/4
    t11 = (275 + t22 + t21)/4
print("Number of iterations: "+str(15))
print("T11 = "+str(t11))
print("T12 = "+str(t12))
print("T21 = "+str(t21))
print("T22 = "+str(t22))

# Verify
A = np.array([[-4,1,0,1],[1,-4,1,0],[0,1,-4,1],[0,1,1,-4]],dtype=float)
b = np.array([[-225],[-25],[-75],[-275]],dtype=int)
t = np.array([[t12],[t22],[t21],[t11]],dtype=float)

err = np.matmul(A,t)
err = err - b
print("Error:\n"+str(err))