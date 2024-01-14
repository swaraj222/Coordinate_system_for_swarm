import numpy as np
import matplotlib.pyplot as plt

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
num_robots = 5
VST = np.zeros((num_robots - 1, num_robots)) # (Distance from each robot, number of data due to robots)

X = [1, 2, 3, 4, 5]
Y = [1, 2, 3, 4, 5]

j= 0

for i in range(num_robots):
    while j != i:
        VST[i].append(np.sqrt((Y[i]-Y[j])**2 + (X[i]- X[j])**2))
    j = j+1