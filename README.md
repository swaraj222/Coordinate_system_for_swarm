# Coordinate_system_for_swarm
 
The repository contains three files:

VST_generator.py:
Executing this code will generate VST containing the robot id and the distance it is calculating with each of the other robots sequentially according to their ids. The code takes input of custom coordinates, the number of robots and also the standard deviation for the gausian noise it is simulating. The code prints the list of X and Y coordinates of the points as the code can generate random coordinates too.

Algorithm_1.py:
This code generates the VST containg the leader ID and the IDs of the reference robots, and the VST containing the coordinates of the leader and the reference robots. If plt.show() is added at the end of the code then the plot of the positions of robots and then the figure of the selected leader and reference robots is shown.

Coordinate_generator.py:
The code generates the VST containing the coordinates of all the robots on the basis of the new coordinate system and also shows the plot of the positions of robots and then the figure of the selected leader and reference robots is shown.
