import numpy as np
from numpy.linalg import norm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import random

def AnimationFunc(newPoints):
        xx = []
        yy = []
        for j in range(len(newPoints)):
            xx.append(newPoints[j][0])
            yy.append(newPoints[j][1])
        plt.plot(xx, yy,'r')

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

def swapfn(solution,i,j):
    temp = solution[i].copy()
    solution[i] = solution[j].copy()
    solution[j] = temp.copy()
    return solution

def beam_search(points, indices):
    mutated = np.zeros((20,1000))
    mutated = mutated.astype(int)
    combined = []
    currentDistance = []
    indices = indices.astype(int)
    for i in range(0,20):
         position1 = np.arange(0,999)
         random_pos1 = random.choice(position1)
         new_pos = position1.tolist()
         new_pos.remove(random_pos1)
         random_pos2 = random.choice(new_pos)
         mutated[i] = swapfn(indices[i].copy(), random_pos1, random_pos2)
         combined.append(indices[i])
         combined.append(mutated[i])
         currentDistance.append(distanceCal(points[indices[i]]))
         currentDistance.append(distanceCal(points[mutated[i]]))
         
    newList = np.zeros((40,1001))
    for i in range(0,40):
        newList[i][0:1000] = combined[i]
        newList[i][1000] = currentDistance[i]
    sortedList = sorted(newList, key = lambda row : (row[1000],row[0]))
    new_indices = np.zeros((20,1000))
    for i in range(0,20):
        new_indices[i] = sortedList[i][0:1000]
    
    return new_indices, sortedList[0][1000]

def main():
    points = np.loadtxt("tsp.txt", delimiter=',', dtype=float)
    indices = np.zeros((20,1000))
    for i in range(0,20):
        indices[i] = np.arange(0,1000)
        np.random.shuffle(indices[i])
    Evals = 1000 
    indices = indices.astype(int)
    final_indices = np.zeros((Evals,1000))
    final_indices[0] = indices[0]
    bestDistance = [distanceCal(points[indices[0]])]
    newPoints = [points[indices[0]]]
    for i in range (1,Evals):
        print("Eval", i)
        fig = plt.figure()
        indices, currentDistance = beam_search(points.copy(), indices.copy())
        if currentDistance < bestDistance[i-1]:
            bestDistance.append(currentDistance)
            final_indices[i] = indices[0]
        else:
            bestDistance.append(bestDistance[i-1])
            final_indices[i] = final_indices[i-1]
        final_indices = final_indices.astype(int)
        newPoints.append(points[final_indices[i]])
        AnimationFunc(newPoints[i])
        animator = ani.FuncAnimation(fig, AnimationFunc)
        plt.show()
    x = np.arange(0,Evals)
    plt.plot(x,bestDistance,'-')
    #print(bestDistance[-1])
    #dataExport = ' '.join(map(str,bestDistance))
    #with open('TSP_BS_values_long.txt', 'w') as f:
       # f.write(dataExport)

if __name__ == "__main__":
    main() 
    
