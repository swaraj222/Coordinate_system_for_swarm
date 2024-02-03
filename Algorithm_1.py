import numpy as np 
import matplotlib.pyplot as plt
from VST_generator import VST, num_robots, X, Y

R = 4.5 # Initial radius to check for neighbours

def neighbour_count(VST, id, R): # Function for checking the neighbour of the each robot
    count = 0
    j = VST[f'{id}_dist']
    for i in j:
        if i < R:
            count += 1
    return count

def neighbour_check(VST, num_robots, R): # Function for making the list for neighbour count
    n_count = []
    for i in range(num_robots):
        n_count.append(neighbour_count(VST, i, R))
    return n_count

n_count = neighbour_check(VST, num_robots , R)

def n_unique_count(n_count): # Checking that neighbour counts are not repetitive
    sorted_n_count = sorted(n_count, reverse = True)

    if sorted_n_count[0] == sorted_n_count[1]:
        return True
    elif sorted_n_count[2] == sorted_n_count[3]:
        return True
    else:
        return False

def n_list_final(VST, num_robots, R): # Finalising the neighbour count list
    n_count = neighbour_check(VST, num_robots, R)
    stop = 0
    while n_unique_count(n_count):
        R = R - 0.01
        if stop > 200:
            break
        n_count = neighbour_check(VST, num_robots, R)
        stop = stop + 1
    return n_count

n_count = n_list_final(VST, num_robots, R)
print("Neighbour count of each robot", n_count)
leader_id = 0 # Proposing a leader ID
l = 0

bid = n_count[0]
leader_bid = n_count[leader_id]

# Finding the leader ID
while l < num_robots: 
    bid = n_count[l]
    if bid <= leader_bid:
        leader_id = leader_id
    else:
        leader_bid = bid
        leader_id = l
    l += 1

VST['Leader_id']= leader_id # Adding the leader ID to VST
robots_list = sorted(VST[f'{leader_id}_dist']) # Listing the distance of each robots from the leader robot

def ref_select(VST, leader_id, robots_list): # Function for selecting the reference robots
    ref_robot = True
    ref_rob_a_id = 0 # Prposing reference robots ID
    ref_rob_b_id = 1
    while ref_robot: 
        a_dist = robots_list[ref_rob_a_id]
        b_dist = robots_list[ref_rob_b_id]
        if a_dist == b_dist:
            ref_rob_b_id +=1

        a_index = VST[f'{leader_id}_dist'].index(a_dist)
        b_index = VST[f'{leader_id}_dist'].index(b_dist)

        if a_dist == b_dist:
            b_index +=1
        if a_index >= leader_id:
            a_index += 1
        if b_index >= leader_id:
            b_index += 1
        
        if b_index > a_index:
            ab_dist = VST[f'{a_index}_dist'][b_index - 1]
        else:
            ab_dist = VST[f'{a_index}_dist'][b_index]
        
        if ab_dist - 0.05 <  a_dist + b_dist and a_dist + b_dist < ab_dist + 0.05:   # Checking for colinearity with leader robot
            ref_robot = True
            ref_rob_b_id += 1
            print("In a line")
        else:
            ref_robot = False
            return a_index, b_index

ref_rob_a_id, ref_rob_b_id = ref_select(VST, leader_id, robots_list)

VST['Reference Robot a'] = ref_rob_a_id # Adding reference robots ID to VST
VST['Reference Robot b'] = ref_rob_b_id

print("Leader ID = ", leader_id)
print("Reference Robot a = ", ref_rob_a_id)
print("Reference Robot b = ", ref_rob_b_id)

def dist(VST, i, j): # Function for finding distance between robot i and j
    if j>i:
        j -= 1
    distance = VST[f'{i}_dist'][j]
    return distance


z_la = dist(VST, leader_id, ref_rob_a_id) # Distance between leader and reference robot a
z_lb = dist(VST, leader_id, ref_rob_b_id) # Distance between leader and reference robot b
z_ab = dist(VST, ref_rob_a_id, ref_rob_b_id) # Distance between reference robot a and reference robot b

x_a = round(1/2*(z_ab + ((z_la**2 - z_lb**2)/z_ab)), 4)
x_b = round(1/2*(((z_la**2 - z_lb**2)/z_ab) - z_ab), 4)
y_l = round(np.sqrt(abs(z_la**2 - x_a**2)), 4)

print("The co-ordinates are, for leader",(0, y_l),"\n for reference robtot a is", (x_a, 0),"\n for reference robtot b is",(x_b, 0) )

VST["Leader co-ordinate"] = (0, y_l)
VST["Reference robot a co-ordinate"] = (x_a, 0)
VST["Reference robot b co-ordinate"] = (x_b, 0)

print("VST at the end of algorithm 1: \n",VST)

plt.figure(2)
plt.title("Position of robots in space with Leader and reference robots selected")
plt.scatter(X,Y)
plt.xlabel("X co-ordinate")
plt.ylabel("Y co-ordinate")
plt.scatter(X[ref_rob_a_id],Y[ref_rob_a_id],c='orange')
plt.annotate(f"Reference robot a = ({x_a}, 0)", 
                 (X[ref_rob_a_id],Y[ref_rob_a_id]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')
plt.scatter(X[ref_rob_b_id],Y[ref_rob_b_id],c='orange')
plt.annotate(f"Reference robot b = ({x_b}, 0)", 
                 (X[ref_rob_b_id],Y[ref_rob_b_id]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')
plt.scatter(X[leader_id],Y[leader_id],c='red')
plt.annotate(f"Leader robot = (0, {y_l})", 
                 (X[leader_id],Y[leader_id]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')
plt.axline([X[ref_rob_a_id], Y[ref_rob_a_id]], [X[ref_rob_b_id], Y[ref_rob_b_id]])


        
# plt.show()