# import numpy as np

# def trilateration(P1, P2, P3, r1, r2, r3):

#   p1 = np.array([0, 0, 0])
#   p2 = np.array([P2[0] - P1[0], P2[1] - P1[1], P2[2] - P1[2]])
#   p3 = np.array([P3[0] - P1[0], P3[1] - P1[1], P3[2] - P1[2]])
#   v1 = p2 - p1
#   v2 = p3 - p1

#   Xn = (v1)/np.linalg.norm(v1)

#   tmp = np.cross(v1, v2)

#   Zn = (tmp)/np.linalg.norm(tmp)

#   Yn = np.cross(Xn, Zn)

#   i = np.dot(Xn, v2)
#   d = np.dot(Xn, v1)
#   j = np.dot(Yn, v2)

#   X = ((r1**2)-(r2**2)+(d**2))/(2*d)
#   Y = (((r1**2)-(r3**2)+(i**2)+(j**2))/(2*j))-((i/j)*(X))
#   Z1 = np.sqrt(max(0, r1**2-X**2-Y**2))
#   Z2 = -Z1

#   K1 = P1 + X * Xn + Y * Yn + Z1 * Zn
#   K2 = P1 + X * Xn + Y * Yn + Z2 * Zn
#   return K1,K2

# point1 = (0, 0, 0)
# point2 = (4, 0, 0)
# point3 = (0, 3, 0)

# distance1 = 5
# distance2 = 4
# distance3 = 3

# result = trilateration(point1, point2, point3, distance1, distance2, distance3)
# print(f'Target Point Coordinates: {result}')

import numpy as np

def trilateration_2d(P1, P2, P3, r1, r2, r3):
    p1 = np.array([0, 0])
    p2 = np.array([P2[0] - P1[0], P2[1] - P1[1]])
    p3 = np.array([P3[0] - P1[0], P3[1] - P1[1]])
    v1 = p2 - p1
    v2 = p3 - p1

    Xn = (v1) / np.linalg.norm(v1)

    tmp = np.cross(v1, v2)

    Yn = (tmp) / np.linalg.norm(tmp)

    # Yn = np.cross(Xn, Zn)

    i = np.dot(Xn, v2)
    d = np.dot(Xn, v1)
    j = np.dot(Yn, v2)

    X = ((r1**2) - (r2**2) + (d**2)) / (2 * d)
    Y = (((r1**2) - (r3**2) + (i**2) + (j**2)) / (2 * j)) - ((i / j) * (X))

    # Z coordinate is not applicable in 2D
    Z1, Z2 = 0, 0

    K1 = P1 + X * Xn + Y * Yn # + Z1 * Zn
    K2 = P1 + X * Xn + Y * Yn # + Z2 * Zn
    return K1, K2

# Example usage
P1 = np.array([0, 0])
P2 = np.array([4, 0])
P3 = np.array([0, 3])

r1 = 5
r2 = 3
r3 = 4

result = trilateration_2d(P1, P2, P3, r1, r2, r3)
print(f'Target Point Coordinates: {result}')
