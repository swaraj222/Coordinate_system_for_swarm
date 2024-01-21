import numpy as np
import matplotlib.pyplot as plt
import random

# class VirtualStigmergyTable:
#     def __init__(self, num_robots):
#         self.num_robots = num_robots
#         self.distance_table = np.zeros((num_robots, num_robots))  # Initialize a 2D array for distances

#     def generate_distance(self, robot1, x_coordinate, y_coordinate):
#         self.distance_table[robot1, robot2] = distance
#         self.distance_table[robot2, robot1] = distance  # Distance is symmetric

#     def retrieve_distance(self, robot1, robot2):
#         return self.distance_table[robot1, robot2]

# def visualize_distance_table(table):
#     plt.imshow(table, cmap='hot', interpolation='nearest')
#     plt.title('Virtual Stigmergy Distance Table')
#     plt.colorbar(label='Distance')
#     plt.show()

# # Example Usage
# if __name__ == "__main__":
num_robots = 10
VST = np.zeros((num_robots, num_robots)) # (Distance from each robot, number of data due to robots)

# print(VST)

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(X)):
    X[i] = random.uniform(0 , 10)
for i in range(len(Y)):
    Y[i] = random.uniform(0 , 10)

X = list(np.around(X,2))
Y = list(np.around(Y,2))
# j= 0

for i in range(num_robots):
    for j in range(num_robots):
        if j!=i:
            VST[i][j] = (np.sqrt((Y[i]-Y[j])**2 + (X[i]- X[j])**2))

VST_i= []                         
# np.array(VST_i)
for k in VST:
    for l in k:
        if l == 0.0:
            k = np.delete(k, np.where(k == 0.0))
            k = k.tolist()
            VST_i.append(k)

VST = VST_i 

print("X", X)
print("Y", Y)
plt.scatter(X,Y)
