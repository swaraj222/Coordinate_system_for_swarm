import numpy as np
import matplotlib.pyplot as plt
from Algorithm_1 import VST, num_robots

Leader_coordinate = VST["Leader co-ordinate"] 
Ref_rob_a = VST["Reference robot a co-ordinate"] 
Ref_rob_b = VST["Reference robot b co-ordinate"] 
Leader_id = VST['Leader_id']
Ref_rob_a_id = VST['Reference Robot a']
Ref_rob_b_id = VST['Reference Robot b']

Leader_coordinate = list(Leader_coordinate)
Leader_coordinate.append(0)
Leader_coordinate = tuple(Leader_coordinate)

Ref_rob_a = list(Ref_rob_a)
Ref_rob_a.append(0)
Ref_rob_a = tuple(Ref_rob_a)

Ref_rob_b = list(Ref_rob_b)
Ref_rob_b.append(0)
Ref_rob_b = tuple(Ref_rob_b)

def trilaterate(point1, distance1, point2, distance2, point3, distance3):
    # Convert points to numpy arrays for easy calculations
    p1 = np.array(point1)
    p2 = np.array(point2)
    p3 = np.array(point3)

    # Calculate vectors and distances
    d1 = distance1
    d2 = distance2
    d3 = distance3

    # Vectors pointing from point1 to point2 and point3
    ex = (p2 - p1) / np.linalg.norm(p2 - p1)
    i = np.dot(ex, p3 - p1)
    ey = (p3 - p1 - i * ex) / np.linalg.norm(p3 - p1 - i * ex)
    ez = np.cross(ex, ey)

    # Calculate the coordinates of the target point
    j = np.dot(ey, p3 - p1)
    x = (d1**2 - d2**2 + i**2) / (2 * i)
    y = (d1**2 - d3**2 + i**2 + j**2) / (2 * j) - (i / j) * x

    # Calculate the z-coordinate (if working in 3D)
    z = np.sqrt(d1**2 - x**2 - y**2)

    # Coordinates of the target point
    target_point = p1 + x * ex + y * ey + z * ez

    return target_point

def trilateration(P1, r1, P2, r2, P3, r3):

  p1 = np.array([0, 0, 0])
  p2 = np.array([P2[0] - P1[0], P2[1] - P1[1], P2[2] - P1[2]])
  p3 = np.array([P3[0] - P1[0], P3[1] - P1[1], P3[2] - P1[2]])
  v1 = p2 - p1
  v2 = p3 - p1

  Xn = (v1)/np.linalg.norm(v1)

  tmp = np.cross(v1, v2)

  Zn = (tmp)/np.linalg.norm(tmp)

  Yn = np.cross(Xn, Zn)

  i = np.dot(Xn, v2)
  d = np.dot(Xn, v1)
  j = np.dot(Yn, v2)

  X = ((r1**2)-(r2**2)+(d**2))/(2*d)
  Y = (((r1**2)-(r3**2)+(i**2)+(j**2))/(2*j))-((i/j)*(X))
  Z1 = np.sqrt(max(0, r1**2-X**2-Y**2))
  Z2 = -Z1

  K1 = np.around(P1 + X * Xn + Y * Yn + Z1 * Zn, 4)
  K2 = P1 + X * Xn + Y * Yn + Z2 * Zn

  K1 = np.delete(K1, 2)
  K1 = tuple(K1)
  return K1

for id in range(num_robots):
    if id!=Leader_id and id != Ref_rob_a_id and id != Ref_rob_b_id:
        if Leader_id > id:
            Rel_Leader_id = Ref_rob_a_id - 1
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
        VST[f'{id}_coordinates'] = trilateration(Leader_coordinate, L_dist, Ref_rob_a, a_dist, Ref_rob_b, b_dist)
#result = trilaterate(point1, distance1, point2, distance2, point3, distance3)
#print(f'Target Point Coordinates: {result}')
print(VST)
plt.show()
