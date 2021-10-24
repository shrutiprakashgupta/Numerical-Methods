# To solve: Temperature as a function of time and space 
# Explicit method to solve Parabolic PDE

import numpy as np
from matplotlib import pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

# Parameters: 
Cp = 0.2174     #cal/gC
p = 2.7         #g/cm^3
k = 0.49        #cal/s-cm-C

#Ti(n+1) = Ti(n) + (a*del_t)/(del_x^2)[Ti+1(n) - 2Ti(n) + Ti-1(n)]

# Setting the parameters for evaluation 
a = (p*Cp)/k
del_t = 0.01     #sec
del_x = 1       #cm
alpha = (a*del_t)/(math.pow(del_x,2))
L = 10          #cm
T_win = 20      #sec - The time window for evaluation of the PDE

Temp = np.zeros((int(T_win/del_t)+1,int(L/del_x)+1))
Temp[0,0] = 100
Temp[0,-1] = 50     #Setting the initial conditions 

TDMA_mat = np.zeros((np.size(Temp,1),np.size(Temp,1)))
TDMA_mat[0,0] = 1
TDMA_mat[-1,-1] = 1
for i in range(1,np.size(TDMA_mat,0)-1):
    TDMA_mat[i,i-1] = alpha
    TDMA_mat[i,i] = 1 - 2*alpha
    TDMA_mat[i,i+1] = alpha

def explicit_method(Tn):
    Tn_1 = np.transpose(np.matmul(TDMA_mat,np.transpose(Tn)))
    return Tn_1

for i in range(np.size(Temp,0)-1):
    Temp[i+1] = explicit_method(Temp[i])
    
x = np.linspace(0, L+del_x, int(L/del_x)+1)
y = np.linspace(0, T_win+del_t, int(T_win/del_t)+1)

X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Temp, cmap='viridis', edgecolor='none')
ax.set_title('Time Evolution of the Temperature distribution')
ax.set_xlabel('Length (in cm)')
ax.set_ylabel('Time (in sec)')
plt.show()