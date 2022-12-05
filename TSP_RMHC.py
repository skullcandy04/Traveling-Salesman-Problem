import numpy as np
from numpy.linalg import norm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import random
from numba import jit, cuda

@jit(target_backend='cuda')
def AnimationFunc(newPoints):
        xx = []
        yy = []
        for j in range(len(newPoints)):
            xx.append(newPoints[j][0])
            yy.append(newPoints[j][1])
        plt.plot(xx, yy,'r')

@jit(target_backend='cuda')
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

@jit(target_backend='cuda')
def bestSwapSol(points,cd):
    tempList = points.copy()
    position1 = np.arange(0,999)
    random_pos1 = random.choice(position1)
    new_pos = position1.tolist()
    new_pos.remove(random_pos1)
    random_pos2 = random.choice(new_pos)
    newList = swapfn(tempList.copy(),random_pos1,random_pos2)
    currentDistance = distanceCal(newList)
    #print("**")
    #print(currentDistance)
    return newList, tempList, currentDistance

def main():
    points = np.loadtxt("tsp.txt", delimiter=',', dtype=float)
    np.random.shuffle(points)
    bestDistance = [distanceCal(points)]
    Evals = 1000
    cd = 0
    newPoints = [points]
    for i in range(1,Evals):
        print("Eval ",i)
        fig = plt.figure()
        newList, tempList, currentDistance = bestSwapSol(points,cd)
        if currentDistance < bestDistance[i-1]:
            bestDistance.append(currentDistance)
            points = newList
        else:
            bestDistance.append(bestDistance[i-1])
            points = tempList
        newPoints.append(points)
        AnimationFunc(newPoints[i])
        animator = ani.FuncAnimation(fig, AnimationFunc)
        plt.show()
    x = np.arange(0,Evals)
    plt.plot(x,bestDistance,'-')
    print(bestDistance)
    #print(points)
    '''
    dataExport = ' '.join(map(str,bestDistance))
    with open('TSP_RMHC_values_long.txt', 'w') as f:
        f.write(dataExport)
    '''
if __name__ == "__main__":
    main()       