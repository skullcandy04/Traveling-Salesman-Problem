import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import random
import math



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
    
def crossOver(points,indices,k):
    i = k
    j = k + 1
    p1 = indices[i]
    p2 = indices[j]
    c = []
    cP1 = []
    cP2 = []
    
    gA = int(random.random() * len(p1))
    gB = int(random.random() * len(p1))
    
    startG = min(gA, gB)
    endG = max(gA, gB)

    for i in range(startG, endG):
        cP1.append(p1[i])
        
    cP2 = [item for item in p2 if item not in cP1]

    c = cP1 + cP2
    return c
    
def geneticAlgo(points, indices):
    new_indices = indices.copy()
    np.random.shuffle(new_indices)
    cross_over = np.zeros((7,1000))
    mutated = np.zeros((3,1000))
    mutated = mutated.astype(int)
    cross_over = cross_over.astype(int)
    new_indices = new_indices.astype(int)
    recombined = []
    currentDistance = []
    for i in range(0,20):
        if i<7:
            cross_over[i] = crossOver(points.copy(),new_indices.copy(), i)
            recombined.append(cross_over[i])
            currentDistance.append(distanceCal(points[cross_over[i]]))
        elif i>=7 and i<10:
            position1 = np.arange(0,999)
            random_pos1 = random.choice(position1)
            new_pos = position1.tolist()
            new_pos.remove(random_pos1)
            random_pos2 = random.choice(new_pos)
            mutated[i-7] = swapfn(new_indices[i-7].copy(), random_pos1, random_pos2)
            recombined.append(mutated[i-7])
            currentDistance.append(distanceCal(points[mutated[i-7]]))
        else:
            recombined.append(new_indices[i-10])
            currentDistance.append(distanceCal(points[new_indices[i-10]]))

    newList = np.zeros((20,1001))
    for i in range(0,20):
        newList[i][0:1000] = recombined[i]
        newList[i][1000] = currentDistance[i]
    sortedList = sorted(newList, key = lambda row : (row[1000],row[0]))
    latest_indices = np.zeros((10,1000))
    for i in range(0,10):
        latest_indices[i] = sortedList[i][0:1000]
    
    return latest_indices, sortedList[0][1000]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
def main():
    
    points = np.loadtxt("tsp.txt", delimiter=',', dtype=float)
    indices = np.zeros((10,1000))
    Evals = 100000
    for i in range(0,10):
        indices[i] = np.arange(0,1000)
        np.random.shuffle(indices[i])
    indices = indices.astype(int)
    final_indices = np.zeros((Evals,1000))
    final_indices[0] = indices[0]
    newPoints = [points[indices[0]]]
    bestDistance = [distanceCal(points[indices[0]])]
    for i in range(1,Evals):
        fig = plt.figure()
        print("Eval", i)
        indices, currentDistance = geneticAlgo(points.copy(), indices.copy())
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
    
    #print(bestDistance)
    #dataExport = ' '.join(map(str,bestDistance))
    #with open('TSC_DC_values_long.txt', 'w') as f:
    #    f.write(dataExport)
    
if __name__ == "__main__":
    main()
    
    