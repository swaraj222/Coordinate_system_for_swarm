import numpy as np
import matplotlib.pyplot as plt
import random

num_robots = 7
VST_list = np.zeros((num_robots, num_robots)) # (Distance from each robot, number of data due to robots)
VST = {}
# print(VST)

# X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Y = [1, 2, 3, 5, 5, 6, 7, 8, 9, 10]

# X = [4.5608, 2.5501, 4.0817, 1.3471, 9.7813, 5.5381, 4.5892, 8.5662, 6.0688, 4.5492]
# Y = [8.0918, 7.4495, 5.2037, 0.8356, 7.521, 0.0171, 2.4966, 4.6773, 4.6039, 0.4696]

X = [1,2,3,4,5,6,7]
Y = [1,2,3,4,5,6,7]

for i in range(len(X)):
    X[i] = random.uniform(0 , 10)
for i in range(len(Y)):
    Y[i] = random.uniform(0 , 10)

print("X", X)
print("Y", Y)


X = list(np.around(X,4))
Y = list(np.around(Y,4))
# j= 0

for i in range(num_robots):
    for j in range(num_robots):
        if j!=i:
            VST_list[i][j] = round(np.sqrt((Y[i]-Y[j])**2 + (X[i]- X[j])**2), 4)

print(VST_list)
# print(original_data)

            #print(j)


VST_i= []                         
# np.array(VST_i)
# for k in range(len(VST_list)):
#     for l in range(len(VST_list[k])):
#         if VST_list[k][l] == 0.0:
#             VST_list[k] = np.delete(VST_list[k], np.where(VST_list[k][l] == 0.0))
#             VST_list[k] = VST_list[k].tolist()
#             VST_i.append(k)

for k in range(len(VST_list)):
    li_te = list(VST_list[k])
    li_te.pop(k)
    VST_i.append(li_te) 
    # np.delete(VST_list[k], np.where(VST_list[k] == 0.0)[0])
    # for l in range(len(VST_list[k])):
    #     if VST_list[k][l] == 0.0:
            
    #         VST_list[k] = VST_list[k].tolist()
    #         VST_i.append(k)

print(VST_i)
for i in range(len(VST_i)):
    for j in range(len(VST_i[i])):
        gaussian_noise = round(np.random.normal(0, 0.4), 4)
        scaling_factor = j/round(10*np.sqrt(2), 4)
        VST_i[i][j] += round(gaussian_noise * scaling_factor, 4)

print(VST_i)
# VST_i = list(np.around(np.array(VST_i), 4))
# VST_i = [ '%.4f' % elem for elem in VST_i ]

for i in range(len(VST_i)):
    VST_i[i] = [ round(elem, 4) for elem in VST_i[i] ]
    VST[f'{i}_dist'] = VST_i[i]
VST = np.array(VST)
print(VST)
# print(VST_list)

print("X", X)
print("Y", Y)

plt.figure(1)
plt.scatter(X,Y)
