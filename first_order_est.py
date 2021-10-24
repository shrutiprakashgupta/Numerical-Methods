# Approximation
import numpy as np
from matplotlib import pyplot as plt

#The difference equation generated with the given relation, parameters and the initial conditions is 
# c[n+1] = c[n] - k*c[n]*h

# Parameter 
k  = 0.2    #per day
h = 0.1     #day

# initial conditions  
t_init = 0
c_init = 10

# Duration for evalution
t_final = 1

# Output vector
t = np.zeros((1,int((t_final-t_init)/h)+1))
c = np.zeros((1,int((t_final-t_init)/h)+1))

t[0,0] = t_init
c[0,0] = c_init

for i in range(1,len(c[0])):
    c[0,i] = c[0,i-1]  - k*c[0,i-1]*h
    t[0,i] = t[0,i-1] + h

c[0] = np.round(c[0], 3)

print("The concentration at time steps of "+str(h)+" from "+str(t_init)+" to "+str(t_final)+" are: ")
print(np.transpose(c))

log_c = np.log(c[0])

# Determining the slope of the semilog graph
slope = float(0)
for i in range(1,len(log_c)):
    slope = slope + ((log_c[i]-log_c[i-1])/h)
slope = slope / (len(log_c)-1)
plt.plot(t[0],log_c)
plt.xlabel("t (in day)")
plt.ylabel("ln c (c in Baquerel per litre)")
plt.title("Semilog graph of concentration vs time")
plt.show()

print("The slope of the semi-log graph is: "+str(slope))