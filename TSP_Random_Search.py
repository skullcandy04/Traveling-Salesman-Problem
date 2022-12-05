import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance
import math

points = np.loadtxt("tsp.txt", delimiter=',', dtype=float)

#for i in range(0,len(points)):
    #plt.plot(points[i][0],points[i][1],'.')

def distanceCal(points1):
    d = points1.copy()
    d1 = np.zeros((1000, 2))
    d1[0:999, :] = d[1:1000, :].copy()
    d1[999, :] = d[0:1, :].copy()
    df = d1 - d
    dx = df[:, 0]
    dy = df[:, 1]
    d_tot = np.power((np.power(dx, 2) + np.power(dy, 2)), 0.5)
    d_tot = np.sum(d_tot)
    return d_tot

x = []
y = []
for k in range (0,1):
    distance_tot = [math.inf]
    Evals = 1000
    for i in range (1,Evals+1):
        print("Eval", i)
        np.random.shuffle(points)
        distance1 = distanceCal(points)
        if distance1 < distance_tot[i-1]:
            distance_tot.append(distance1)
        else :
            distance_tot.append(distance_tot[i-1])
    y.append(distance_tot[1:len(distance_tot)])
    x.append(np.arange(1,Evals+1))
    plt.plot(x[k], y[k])
'''
dataExport = ' '.join(map(str,y[k]))
with open('TSP_random_values.txt', 'w') as f:
    f.write(dataExport)
'''
plt.show()

