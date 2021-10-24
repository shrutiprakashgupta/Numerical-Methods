# To solve: Temperature as a function of time and space 
# Implicit method to solve Parabolic PDE

import numpy as np
from matplotlib import pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

# Parameters: 
Cp = 0.2174     #cal/gC
p = 2.7         #g/cm^3
k = 0.49        #cal/s-cm-C

# Ti-1(n+1)(-lambda) + Ti(n+1)(1+2*lambda) + Ti+1(n+1)(-lambda) = Ti(n)

# Setting the parameters for evaluation 
a = (p*Cp)/k
del_t = 0.01      #sec
del_x = 1        #cm
l = (a*del_t)/(math.pow(del_x,2))      
L_win = 10          #cm
T_win = 20          #sec - The time window for evaluation of the PDE

Temp = np.zeros((int(T_win/del_t)+1,int(L_win/del_x)+1))
Temp[:,0] = 100
Temp[:,-1] = 50     #Setting the initial conditions 

TDMA_1 = np.array([-(l/2) for i in range(np.size(Temp,1)-3)])
TDMA_2 = np.array([1+l for i in range(np.size(Temp,1)-2)])
TDMA_3 = np.array([-(l/2) for i in range(np.size(Temp,1)-3)])

def Thomas_method(A_1,A_2,A_3):
# Applying Thomas Method
    L = np.zeros((np.size(A_2),np.size(A_2)),dtype=float)
    U = np.zeros((np.size(A_2),np.size(A_2)),dtype=float)
    L[0,0] = 1
    U[0,0] = A_2[0]
    f = A_2[0]
    for i in range(1,np.size(A_2)):
        e = A_1[i-1]/f
        f = A_2[i-1] - e*A_3[i-1]
        L[i,i-1] = e
        L[i,i] = 1
        U[i,i] = f  
        U[i-1,i] = A_3[i-1]
    return L,U
    
def Propagate(A,X,B,back):
    n = np.size(A,0)
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

L,U = Thomas_method(TDMA_1,TDMA_2,TDMA_3)
n = np.size(Temp,1)

for i in range(np.size(Temp,0)-1):    
    X = np.array([[0.0,i] for i in range(n-2)])
    D = np.zeros((n-2,1),dtype=float)
    B = np.zeros(n-2,dtype=float)
        
    B[1:-1] = (l*Temp[i,1:-3])/2 + (1-l)*Temp[i,2:-2] + (l*Temp[i,3:-1])/2
    B[0] = (l*Temp[i,0]) + (1-l)*Temp[i,1] + (l*Temp[i,2])/2
    B[-1] = (l*Temp[i,-3])/2 + (1-l)*Temp[i,-2] + (l*Temp[i,-1])
    D = Propagate(L,D,B,0)
    X[:,0] = Propagate(U,X[:,0],D,1)
    X = [sorted(X,key=lambda x:x[1])[i][0] for i in range(len(X))]
    Temp[i+1,1:-1] = X

x = np.linspace(0, L_win+del_x, int(L_win/del_x)+1)
y = np.linspace(0, T_win+del_t, int(T_win/del_t)+1)

X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Temp, cmap='viridis', edgecolor='none')
ax.set_title('Time Evolution of the Temperature distribution')
ax.set_xlabel('Length (in cm)')
ax.set_ylabel('Time (in sec)')
plt.show()