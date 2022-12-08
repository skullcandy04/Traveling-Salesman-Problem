# Traveling-Salesman-Problem

Traveling Salesman Problem is a

Evolutionary Algorithms are best suited for problems that are hard to solve and easy to test. The TSP is one example of this kind where it does not take much time to calculate the goal, which is the total length of the path. This means that for every iteration it is possible to improve/optimize the parameters by calcuting the current goal and comparing it with the previous one.

Here, a comparison between 4 different methods:

1. Random Search
2. Random Mutation Hill Climber (RMHC)
3. Beam Search (just Mutation)
4. Genetic Algorithm (Cross over + mutation)

was performed to validate the efficiencies of the methods. Theoritically, the expected performance was ranked in the order Random Search (worst) < RMHC < Beam Search < Genetic Algorithm (best) and the results from the code also seem to prove them. 

The performance charts can be seen below:

Fitness = -(best path length)

<p aligh="center">
    <img src="/images/RandomSearch_Fitness.png" alt="Alt text" title="Random Search">
    Random Search Fitness
</p>

<p aligh="center">
    <img src="/images/RHMC_Fitness.png" alt="Alt text" title="RHMC">
    RHMC
</p>

<p aligh="center">
    <img src="/images/BeamSearch_Fitness.png" alt="Alt text" title="Beam Search">
    Beam Search Fitness
</p>

<p aligh="center">
    <img src="/images/GA_Fitness.png" alt="Alt text" title="GA Search">
    GA Fitness
</p>
