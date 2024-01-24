import numpy as np 
import math
import time
import matplotlib.pyplot as plt
from VST_generator import VST, num_robots

R = 4

def neighbour_count(VST, id, R):
    count = 0
    j = VST[id]
    for i in j:
        if i < R:
            count+=1
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

robots_list = sorted(VST[leader_id], reverse=True)

print(robots_list)



def ref_select(VST, leader_id, robots_list):
    ref_robot = True
    while ref_robot == True:
        ref_rob_a_id = 0
        ref_rob_b_id = 1
        a_dist = robots_list[ref_rob_a_id]
        b_dist = robots_list[ref_rob_b_id]
        a_indent = np.where(VST[leader_id] == a_dist)
        b_indent = np.where(VST[leader_id] == b_dist)

        print(a_indent)
        print(b_indent)

        if a_indent > leader_id:
            a_indent += 1
        if b_indent > leader_bid:
            b_indent += 1
        ab_dist = VST[a_indent][b_indent]
        
        print(ref_rob_a_id)
        print(ref_rob_b_id)

        if ab_dist ==   a_dist + b_dist:   
            ref_robot = True
            ref_rob_b_id += 1
        else:
            ref_robot = False
            # return ref_rob_a_id, ref_rob_b_id

# ref_rob_a_id, ref_rob_b_id = ref_select(VST, leader_id, robots_list)
ref_select(VST, leader_id, robots_list)
# print(ref_rob_a_id)
# print(ref_rob_b_id)
print(leader_id)
plt.show()

