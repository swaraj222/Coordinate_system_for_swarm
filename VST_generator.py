import numpy as np
import matplotlib.pyplot as plt
import random

num_robots = 10
VST_list = np.zeros((num_robots, num_robots)) # (Distance from each robot, number of data due to robots)
VST = {}
# print(VST)

# X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Y = [1, 2, 3, 5, 5, 6, 7, 8, 9, 10]

X = [4.5608, 2.5501, 4.0817, 1.3471, 9.7813, 5.5381, 4.5892, 8.5662, 6.0688, 4.5492]
Y = [8.0918, 7.4495, 5.2037, 0.8356, 7.521, 0.0171, 2.4966, 4.6773, 4.6039, 0.4696]

for i in range(len(X)):
    X[i] = random.uniform(0 , 10)
for i in range(len(Y)):
    Y[i] = random.uniform(0 , 10)

print("X", X)
print("Y", Y)

original_data = np.linspace(0, 10, 15)
gaussian_noise = np.random.normal(0, 1, len(original_data))

# Scale the Gaussian noise based on the original data
scaling_factor = original_data / max(original_data)  # Adjust the scaling factor as needed
scaled_gaussian_noise = gaussian_noise * scaling_factor

# Add the scaled Gaussian noise to the original data
noisy_data = original_data + scaled_gaussian_noise

X = list(np.around(X,4))
Y = list(np.around(Y,4))
# j= 0

for i in range(num_robots):
    for j in range(num_robots):
        if j!=i:
            VST_list[i][j] = np.sqrt((Y[i]-Y[j])**2 + (X[i]- X[j])**2)

for i in VST_list:
    for j in VST_list:
        
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
