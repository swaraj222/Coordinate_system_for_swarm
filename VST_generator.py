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
VST_list = np.zeros((num_robots, num_robots)) # (Distance from each robot, number of data due to robots)
VST = {}
# print(VST)

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [1, 2, 3, 5, 5, 6, 7, 8, 9, 10]

# X = [4.5608, 2.5501, 4.0817, 1.3471, 9.7813, 5.5381, 4.5892, 8.5662, 6.0688, 4.5492]
# Y = [8.0918, 7.4495, 5.2037, 0.8356, 7.521, 0.0171, 2.4966, 4.6773, 4.6039, 0.4696]

# for i in range(len(X)):
#     X[i] = random.uniform(0 , 10)
# for i in range(len(Y)):
#     Y[i] = random.uniform(0 , 10)

X = list(np.around(X,4))
Y = list(np.around(Y,4))
# j= 0

for i in range(num_robots):
    for j in range(num_robots):
        if j!=i:
            VST_list[i][j] = (np.sqrt((Y[i]-Y[j])**2 + (X[i]- X[j])**2))



VST_i= []                         
# np.array(VST_i)
for k in VST_list:
    for l in k:
        if l == 0.0:
            k = np.delete(k, np.where(k == 0.0))
            k = k.tolist()
            VST_i.append(k)

# VST_i = list(np.around(np.array(VST_i), 4))
# VST_i = [ '%.4f' % elem for elem in VST_i ]

for i in range(len(VST_list)):
    VST_i[i] = [ round(elem, 4) for elem in VST_i[i] ]
    VST[f'{i}_dist'] = VST_i[i]
# print(VST)
# print(VST_list)

print("X", X)
print("Y", Y)

plt.figure(1)
plt.scatter(X,Y)
