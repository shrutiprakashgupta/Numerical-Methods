#Gauss Jordan Elimination 
import numpy as np
import math

# Entering the dimensions of the matrices 
n = 3 
X = np.zeros((n,1),dtype=float)

# Set the matrices 
A = np.array([[9,-4,-2],[4,2,-6],[8,-15,2]],dtype=float)
B = np.array([[0],[-20],[0]],dtype=float)
# X = [[j2], [i2], [i1]]

def Gauss_Jordan_elimination(A,B):
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
                    f = 1
                    break
            if(f==0):
                print("Matrix not Solvable")
                exit(0)                     
    #in case of solvable matrices, after performing the above mentioned swapping procedure, all of the (i,i)th elements would be non-zero
    for i in range(n):
        B[i] = B[i]/A[i,i]
        A[i] = A[i]/A[i,i]
        for j in range(n):
            if(i!=j):
                B[j] = B[j] - A[j,i]*B[i]
                A[j] = A[j] - A[j,i]*A[i]
    return B
  
X = Gauss_Jordan_elimination(A,B)
print("The value of j2 = "+str(B[0]))
print("The value of i1 = "+str(B[1]))
print("The value of i2 = "+str(B[2]))