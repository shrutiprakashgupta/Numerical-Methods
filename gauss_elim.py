# Gauss Elimination Method 
import numpy as np
import math

# Entering the dimensions of the matrices 
n = 3 
X = np.zeros((n,1),dtype=float)

# parameters 
m1 = 50
m2 = 10
m3 = 40
g = 9.8
theta1 = (60*math.pi)/180
theta2 = (30*math.pi)/180
theta3 = (30*math.pi)/180
mu1 = 0.3
mu2 = 0.5
mu3 = 0.2

# Set the matrices 
A_right = np.array([[1,0,m1],[1,-1,-1*m2],[0,1,-1*m3]],dtype=float)
B_right = np.array([[(m1*g)*(math.sin(theta1)-(mu1*math.cos(theta1)))],[(m2*g)*(math.sin(theta2)+(mu2*math.cos(theta2)))],[(m3*g)*(math.sin(theta3)+(mu3*math.cos(theta3)))]],dtype=float)
# X = [[R], [T], [a]]
A_left =  np.array([[1,0,-1*m1],[1,-1,m2],[0,1,m3]],dtype=float)
B_left = np.array([[(m1*g)*(math.sin(theta1)+(mu1*math.cos(theta1)))],[(m2*g)*(math.sin(theta2)-(mu2*math.cos(theta2)))],[(m3*g)*(math.sin(theta3)-(mu3*math.cos(theta3)))]],dtype=float)

def Gauss_elimination(A,B,X):
# Applying Gauss Elimination Method
    for j in range(n):
        for i in range(j+1,n):
            #No need to process if the element is already zero 
            if(A[i,j]!=0):
                #If the preceeding row element is non zero, then only the factor would be defined 
                if(A[i-1,j]!=0):
                    B[i] = B[i] - B[i-1]*(A[i,j]/A[i-1,j])
                    A[i] = A[i] - A[i-1]*(A[i,j]/A[i-1,j])
                #Otherwise, the order of the rows can be swapped
                else:
                    A[i] = A[i]+A[i-1]
                    A[i-1] = A[i]-A[i-1]
                    A[i] = A[i]-A[i-1]
                    B[i] = B[i]+B[i-1]
                    B[i-1] = B[i]-B[i-1]
                    B[i] = B[i]-B[i-1]

    #Back propagation 
    for i in range(n-1,-1,-1):
        X[i] = B[i]
        for j in range(i+1,n):
            X[i] = X[i]-A[i,j]*X[j]
        X[i] = X[i]/A[i,i]
        
    X = np.round(X,4)
    return X

X = Gauss_elimination(A_right,B_right,X)
print("The computed values are: (Assuming the system is moving in right direction")
print("R = "+str(X[0,0]))
print("T = "+str(X[1,0]))
print("a = "+str(X[2,0]))

X = np.zeros((n,1))
X = Gauss_elimination(A_left,B_left,X)
print("The computed values are: (Assuming the system is moving in left direction")
print("R = "+str(X[0,0]))
print("T = "+str(X[1,0]))
print("a = "+str(X[2,0]))