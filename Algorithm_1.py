import numpy as np 
import math
import time
import matplotlib.pyplot as plt
from VST_generator import VST, num_robots, X, Y

R = 2 # Initial radius to check for neighbours

def neighbour_count(VST, id, R):
    count = 0
    j = VST[f'{id}_dist']
    for i in j:
        if i < R:
            count += 1
    return count

def neighbour_check(VST, num_robots, R):
    n_count = []
    for i in range(num_robots):
        n_count.append(neighbour_count(VST, i, R))
    return n_count

n_count = neighbour_check(VST, num_robots , R)

def n_unique_count(n_count):
    sorted_n_count = sorted(n_count, reverse = True)

    if sorted_n_count[0] == sorted_n_count[1]:
        return True
    elif sorted_n_count[2] == sorted_n_count[3]:
        return True
    else:
        return False

def n_list_final(VST, num_robots, R):
    n_count = neighbour_check(VST, num_robots, R)
    stop = 0
    while n_unique_count(n_count):
        R = R - 0.01
        if stop > 150:
            break
        n_count = neighbour_check(VST, num_robots, R)
        stop = stop + 1
    return n_count

n_count = n_list_final(VST, num_robots, R)

leader_id = 0
l = 0

bid = n_count[0]
leader_bid = n_count[leader_id]

while l < num_robots:
    bid = n_count[l]
    if bid <= leader_bid:
        leader_id = leader_id
    else:
        leader_bid = bid
        leader_id = l
    l += 1

VST['Leader_id']= leader_id
robots_list = sorted(VST[f'{leader_id}_dist'])

def ref_select(VST, leader_id, robots_list):
    ref_robot = True
    while ref_robot:
        ref_rob_a_id = 0
        ref_rob_b_id = 1
        a_dist = robots_list[ref_rob_a_id]
        b_dist = robots_list[ref_rob_b_id]
        if a_dist == b_dist:
            ref_rob_b_id +=1

        a_indent = VST[f'{leader_id}_dist'].index(a_dist)
        b_indent = VST[f'{leader_id}_dist'].index(b_dist)

        if a_dist == b_dist:
            b_indent +=1
        if a_indent >= leader_id:
            a_indent += 1
        if b_indent >= leader_bid:
            b_indent += 1
        ab_dist = VST[f'{a_indent}_dist'][b_indent]
        if ab_dist ==   a_dist + b_dist:   
            ref_robot = True
            ref_rob_b_id += 1
            robots_list.pop(1)
            print("In a line")
        else:
            ref_robot = False
            return a_indent, b_indent

ref_rob_a_id, ref_rob_b_id = ref_select(VST, leader_id, robots_list)

VST['Reference Robot a'] = ref_rob_a_id
VST['Reference Robot b'] = ref_rob_b_id

print("Leader ID = ", leader_id)
print("Reference Robot a = ", ref_rob_a_id)
print("Reference Robot b = ", ref_rob_b_id)

def dist(VST, i, j):
    if j>i:
        j -= 1
    distance = VST[f'{i}_dist'][j]
    return distance


z_la = dist(VST, leader_id, ref_rob_a_id)
z_lb = dist(VST, leader_id, ref_rob_b_id)
z_ab = dist(VST, ref_rob_a_id, ref_rob_b_id)

x_a = round(1/2*(z_ab + ((z_la**2 - z_lb**2)/z_ab)), 4)
x_b = round(1/2*(((z_la**2 - z_lb**2)/z_ab) - z_ab), 4)
y_l = round(np.sqrt(z_la - x_a), 4)

print("The co-ordinates are, for leader",(0, y_l),"\n for reference robtot a is", (x_a, 0),"\n for reference robtot b is",(x_b, 0) )

VST["Leader co-ordinate"] = (0, y_l)
VST["Reference robot a co-ordinate"] = (x_a, 0)
VST["Reference robot b co-ordinate"] = (x_b, 0)

print("VST at the end of algorithm 1: \n",VST)

plt.figure(2)
plt.scatter(X,Y)
plt.scatter(X[ref_rob_a_id],Y[ref_rob_a_id],c='orange')
plt.annotate(f"Reference robot a id = {ref_rob_a_id}", 
                 (X[ref_rob_a_id],Y[ref_rob_a_id]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')
plt.scatter(X[ref_rob_b_id],Y[ref_rob_b_id],c='orange',label="Reference robot b")
plt.annotate(f"Reference robot b id = {ref_rob_b_id}", 
                 (X[ref_rob_b_id],Y[ref_rob_b_id]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')
plt.scatter(X[leader_id],Y[leader_id],c='red',label="Leader robot")
plt.annotate(f"Leader robot id = {leader_id}", 
                 (X[leader_id],Y[leader_id]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')


for id in range(num_robots):
    if id!= leader_id and id!= ref_rob_a_id and id!= ref_rob_b_id:
        plt.annotate(f"{id}",
                    (X[id], Y[id]),
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center')