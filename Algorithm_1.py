import numpy as np 
import math
import time

N = 5 # Number of robots

VST = []

def neighbour_count(VST, N):
    for i in range(N):
        VST.