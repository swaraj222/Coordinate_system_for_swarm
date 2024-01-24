import numpy as np 
import math
import time
import matplotlib.pyplot as plt
from VST_generator import VST, num_robots, X, Y

R = 4  # Initial radius to check for neighbours

def neighbour_count(VST, id, R):
    count = 0
    j = VST[f'{id}_dist']
    for i in j:
        if i < R:
            count += 1
    return count

# print("Neighbour count", neighbour_count(VST, 4, R))
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
    print(n_count)
    while n_unique_count(n_count):
        R = R - 0.01
        print("Reducing R", R)
        if stop > 150:
            break
        n_count = neighbour_check(VST, num_robots, R)
        stop = stop + 1
    return n_count

n_count = n_list_final(VST, num_robots, R)


print(n_count)

leader_id = 0
l = 0

bid = n_count[0]
leader_bid = n_count[leader_id]

while l < num_robots:
    bid = n_count[l]
    if bid <= leader_bid:
        print("bid", bid)
        leader_id = leader_id
    else:
        leader_bid = bid
        leader_id = l
    l += 1

VST['Leader_id']= leader_id
robots_list = sorted(VST[f'{leader_id}_dist'])

print(robots_list)



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
        print(a_indent)
        print(b_indent)

        if a_indent >= leader_id:
            a_indent += 1
        if b_indent >= leader_bid:
            b_indent += 1
        ab_dist = VST[f'{a_indent}_dist'][b_indent]
        
        print(a_indent)
        print(b_indent)

        if ab_dist ==   a_dist + b_dist:   
            ref_robot = True
            ref_rob_b_id += 1
            robots_list.pop(1)
            print("In a line")
        else:
            ref_robot = False
            return a_indent, b_indent

# ref_rob_a_id, ref_rob_b_id = ref_select(VST, leader_id, robots_list)
ref_rob_a_id, ref_rob_b_id = ref_select(VST, leader_id, robots_list)

VST['Reference Robot a'] = ref_rob_a_id
VST['Reference Robot b'] = ref_rob_b_id

print(ref_rob_a_id)
print(ref_rob_b_id)
print("Leader ID = ", leader_id)


print(VST)




plt.figure(2)
plt.scatter(X,Y)
plt.scatter(X[ref_rob_a_id],Y[ref_rob_a_id],c='orange')
plt.annotate("Reference robot a", # this is the text
                 (X[ref_rob_a_id],Y[ref_rob_a_id]), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')
plt.scatter(X[ref_rob_b_id],Y[ref_rob_b_id],c='orange',label="Reference robot b")
plt.annotate("Reference robot b", # this is the text
                 (X[ref_rob_b_id],Y[ref_rob_b_id]), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')
plt.scatter(X[leader_id],Y[leader_id],c='red',label="Leader robot")
plt.annotate("Leader robot", # this is the text
                 (X[leader_id],Y[leader_id]), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')
plt.show()

