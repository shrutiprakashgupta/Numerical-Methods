# Explicit Method Inetrpolation
import numpy as np
from matplotlib import pyplot as plt

# Step size
h = 0.1
# Time period
t_0 = 0
t_n = 50
c1_val = np.zeros(int((t_n-t_0)/h)+1)
c2_val = np.zeros(int((t_n-t_0)/h)+1)
c3_val = np.zeros(int((t_n-t_0)/h)+1)
# Initial conditon
c1_val[0] = 1
c2_val[0] = 1
c3_val[0] = 0

# Explicit method
for i in range(int((t_n-t_0)/h)):
    c1_val[i+1] = round(c1_val[i] / (1 + 0.013*h + 1000*h*c3_val[i]),6)
    c2_val[i+1] = round(c2_val[i] / (1 + 2500*h*c3_val[i]),6)
    c3_val[i+1] = round((c3_val[i] - 0.013*h*c1_val[i]) / (1 + 1000*h*c1_val[i] + 2500*h*c2_val[i]),6)
    
fig = plt.figure(1)
plt.plot(c1_val)
plt.title("c1")
plt.show()
plt.close()

fig = plt.figure(2)
plt.plot(c2_val)
plt.title("c2")
plt.show()
plt.close()

fig = plt.figure(3)
plt.plot(c3_val)
plt.title("c3")
plt.show()
plt.close()

fig = plt.figure(4)
plt.plot(c1_val)
plt.plot(c2_val)
plt.title("The concentration of c1 and c2 shown together")
plt.show()
plt.close()

c = [round(c1_val[i]+c2_val[i]+c3_val[i],3) for i in range(len(c1_val))]
fig = plt.figure(4)
plt.plot(c)
plt.title("Sum of concentration of all chemicals involved")
plt.show()
plt.close()