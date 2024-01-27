import numpy as np
import matplotlib.pyplot as plt
from Algorithm_1 import VST, num_robots

Leader_coordinate = VST["Leader co-ordinate"] 
Ref_rob_a = VST["Reference robot a co-ordinate"] 
Ref_rob_b = VST["Reference robot b co-ordinate"] 
Leader_id = VST['Leader_id']
Ref_rob_a_id = VST['Reference Robot a']
Ref_rob_b_id = VST['Reference Robot b']

def trilaterate_2d(p_l, d_l, p_a, d_a, p_b, d_b):
    (x_l, y_l) = p_l
    (x_a, y_a) = (p_a[0], p_a[1])
    (x_b, y_b) = (p_b[0], p_b[1])
    i = 2*x_b - 2*x_l
    j = 2*x_b - 2*x_a
    y = round((((d_l**2 - d_b**2)/i) - ((x_l**2 - x_b**2)/i) - ((y_l**2 - y_b**2)/i) - ((d_a**2 - d_b**2)/j) + ((x_a**2 - x_b**2)/j) + ((y_a**2 - y_b**2)/j)) / (((2*y_b - 2*y_l)/i) - ((2*y_b - 2*y_a)/j)), 4)
    x = round(((d_l**2 - d_b**2)/i) - ((x_l**2 - x_b**2)/i) - ((y_l**2 - y_b**2)/i) - (((2*y_b - 2*y_l)*y)/i), 4)
    return (x,y)

for id in range(num_robots):
    if id!=Leader_id and id != Ref_rob_a_id and id != Ref_rob_b_id:
        if Leader_id > id:
            Rel_Leader_id = Leader_id - 1
        else:
            Rel_Leader_id = Leader_id
        if Ref_rob_a_id > id:
            Rel_Ref_rob_a_id = Ref_rob_a_id - 1
        else:
            Rel_Ref_rob_a_id = Ref_rob_a_id
        if Ref_rob_b_id > id:
            Rel_Ref_rob_b_id = Ref_rob_b_id - 1
        else:
            Rel_Ref_rob_b_id = Ref_rob_b_id
        L_dist = VST[f'{id}_dist'][Rel_Leader_id]
        a_dist = VST[f'{id}_dist'][Rel_Ref_rob_a_id]
        b_dist = VST[f'{id}_dist'][Rel_Ref_rob_b_id]
        VST[f'{id}_coordinates']  = trilaterate_2d(Leader_coordinate, L_dist, Ref_rob_a, a_dist, Ref_rob_b, b_dist)

print("VST with new co-ordinates: \n",VST)
plt.show()
