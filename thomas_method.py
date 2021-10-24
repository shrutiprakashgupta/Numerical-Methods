import numpy as np
import math

# Entering the dimensions of the matrices 
n = 3 
X = np.array([[0.0,i] for i in range(n)])
D = np.zeros((n,1),dtype=float)
res = np.zeros((n,1),dtype=int)

# Set the matrices 
A = np.array([[9,-4,0],[4,2,-6],[8,-15,2]],dtype=float)
B = np.array([[0],[-20],[0]],dtype=float)

def Thomas_method(A,B,X):
# Applying Thomas Method
    #Managing zeros
    for i in range(n-1):
        if(A[i,i]==0):
            f = 0
            for j in range(i+1,n):
                if(A[j,i]!=0):
                    A[i] = A[i]+A[j]
                    A[j] = A[i]-A[j]
                    A[i] = A[i]-A[j]
                    B[i] = B[i]+B[j]
                    B[j] = B[i]-B[j]
                    B[i] = B[i]-B[j]
                    X[i,1] = j
                    X[j,1] = i
                    f = 1
                    break
            if(f==0):
                print("Matrix not Solvable")
                exit(0)
    L = np.zeros((n,n),dtype=float)
    for i in range(n):
        L[i,i] = 1
        for j in range(i+1,n):
            L[j,i] = A[j,i]/A[i,i]
            A[j] = A[j] - L[j,i]*A[i]
    return L,A,B,X

def Propagate(A,X,B,back):
    if(back):
        for i in range(n-1,-1,-1):
            X[i] = B[i]
            for j in range(i+1,n):
                X[i] = X[i]-A[i,j]*X[j]
            X[i] = X[i]/A[i,i]
    else:
        for i in range(n):
            X[i] = B[i]
            for j in range(i):
                X[i] = X[i]-A[i,j]*X[j]
            X[i] = X[i]/A[i,i]
    X = np.round(X,4)
    return X    
L,U,B,X = Thomas_method(A,B,X)
D = Propagate(L,D,B,0)
X[:,0] = Propagate(U,X[:,0],D,1)
X = np.sort(X,axis=1)

print("The original matrix is: \n"+str(A))
print("It is decomposed into: \n"+str(L)+"\n"+str(U))
print("The matrix D is: \n"+str(D))

print("The value of j2 = "+str(X[0]))
print("The value of i2 = "+str(X[1]))
print("The value of i1 = "+str(X[2]))