# This code genertes a VST(Visual Stigmergy Table) that consist of the robot ID and the distance of it from all the other robots
import numpy as np
import matplotlib.pyplot as plt
import random

num_robots = 10 # Setting the number of robots
VST_list = np.zeros((num_robots, num_robots)) # (Distance from each robot, number of data due to robots)
VST = {} 

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [1, 2, 3, 5, 5, 6, 7, 8, 9, 10]

# Randomising the choice of coordinates of the robots

for i in range(len(X)): 
    X[i] = random.uniform(0 , 10)
for i in range(len(Y)):
    Y[i] = random.uniform(0 , 10)

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
plt.scatter(X,Y)
