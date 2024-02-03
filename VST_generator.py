# This code genertes a VST(Visual Stigmergy Table) that consist of the robot ID and the distance of it from all the other robots
import numpy as np
import matplotlib.pyplot as plt
import random

num_robots = 10 # Setting the number of robots
VST_list = np.zeros((num_robots, num_robots)) # (Distance from each robot, number of data due to robots)
VST = {} 

X = [7.7146, 5.2926, 6.253, 1.6542, 0.4861, 6.5201, 7.7541, 0.8125, 3.6631, 2.9394]
Y = [5.4007, 3.3698, 4.6256, 8.628, 7.4055, 8.2469, 3.3499, 0.9888, 0.6216, 2.5005]

# Randomising the choice of coordinates of the robots

# for i in range(len(X)): 
#     X[i] = random.uniform(0 , 10)
# for i in range(len(Y)):
#     Y[i] = random.uniform(0 , 10)

X = list(np.around(X,4))
Y = list(np.around(Y,4))

# Finding the distance from their neighbours
for i in range(num_robots):
    for j in range(num_robots):
        if j!=i:
            VST_list[i][j] = round(np.sqrt((Y[i]-Y[j])**2 + (X[i]- X[j])**2), 4)

VST_i= []                         

# Removing the distance from itself i.e. 0
for k in range(len(VST_list)):
    li_te = list(VST_list[k])
    li_te.pop(k)
    VST_i.append(li_te) 

# Adding scaled Gaussian noise to the data
for i in range(len(VST_i)):
    for j in range(len(VST_i[i])):
        gaussian_noise = round(np.random.normal(0, 0.4), 4)
        scaling_factor = j/round(10*np.sqrt(2), 4)
        VST_i[i][j] += round(gaussian_noise * scaling_factor, 4)

# Adding the data to the VST dictionary
for i in range(len(VST_i)):
    VST_i[i] = [ round(elem, 4) for elem in VST_i[i] ]
    VST[f'{i}_dist'] = VST_i[i]

# Printing the original coordinates of the robots
print("X", X)
print("Y", Y)

# Plotting the original coordintes of the robots
plt.figure(1)
plt.title("Position of robots in space")
plt.scatter(X,Y)

plt.xlabel("X co-ordinate")
plt.ylabel("Y co-ordinate")
