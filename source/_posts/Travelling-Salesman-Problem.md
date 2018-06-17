---
title: Travelling Salesman Problem in Python
date: 2016-12-21 19:05:39
categories: project
tags: python
toc: true
---


Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?
<!-- more -->
NP-hard problem in combinatorial optimization

TSP can be regard as a graph problem can can be modelled as an undirected weighted graph:

| Cities               | Paths             | The path's distance |
| -------------------- | ----------------- | ------------------- |
| the graph's vertices | the graph's edges | the edge's weight   |


It is a minimization problem starting and finishing at a specified vertex after having visited each other vertex exactly once. 


Because the distance in Berlin52.tsp is coordinate distance, so it is a symmetric problem.

And I try to improve the algorithms, so I will introduce some improvement in GA and ACO Algorithm.



## GA
Genetic Algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection.

### Flow chart

![](http://oljkaeely.bkt.clouddn.com/static/image/Travelling-Salesman-Problem/ga-flow.png)


### Result
1000 iterations
![](http://oljkaeely.bkt.clouddn.com/static/image/Travelling-Salesman-Problem/ga_result_1000.jpg)

1000000 iterations with the same rate in GA expression.
![](http://oljkaeely.bkt.clouddn.com/static/image/Travelling-Salesman-Problem/ga_result_1000000.jpg)

So we can find that the rate of descent is really slow. especially campared with other algorithms.

### Improvement
In order to know the parameters' efficiency in the expression, especially in the crossRate and mutationRate, I calculate the crossRate from 0-0.5 stepped by 0.1, mutationRate from 0-0.5 stepped by 0.05, iterations times is 10000, and show the temporary result of each 100 iterations.

![](http://oljkaeely.bkt.clouddn.com/static/image/Travelling-Salesman-Problem/diagram.jpg)
And the calculate the decreate rate of each state, with considering 10 results, using the method of successive minus.
![](http://oljkaeely.bkt.clouddn.com/static/image/Travelling-Salesman-Problem/ga_rate_test.jpg)
![](http://oljkaeely.bkt.clouddn.com/static/image/Travelling-Salesman-Problem/descreate_rate.jpg)

![](http://oljkaeely.bkt.clouddn.com/static/image/Travelling-Salesman-Problem/descreate_rate_2.jpg)

### Conclusion
So we can find that the parameter in expression of GA, if you want to steepest descent to the final result, maybe you can choose crossRate as 0.4 and mutationRate as 0.35.

## ACO
Ants of some species (initially) wander randomly, and upon finding food return to their colony while laying down pheromone trails. If other ants find such a path, they are likely not to keep travelling at random, but instead to follow the trail, returning and reinforcing it if they eventually find food.

Over time, however, the pheromone trail starts to evaporate, thus reducing its attractive strength. The more time it takes for an ant to travel down the path and back again, the more time the pheromones have to evaporate. A short path, by comparison, gets marched over more frequently, and thus the pheromone density becomes higher on shorter paths than longer ones. Pheromone evaporation also has the advantage of avoiding the convergence to a locally optimal solution. If there were no evaporation at all, the paths chosen by the first ants would tend to be excessively attractive to the following ones. In that case, the exploration of the solution space would be constrained. The influence of pheromone evaporation in real ant systems is unclear, but it is very important in artificial systems.

The overall result is that when one ant finds a good (i.e., short) path from the colony to a food source, other ants are more likely to follow that path, and positive feedback eventually leads to all the ants following a single path. The idea of the ant colony algorithm is to mimic this behavior with "simulated ants" walking around the graph representing the problem to solve.

The probability of ants moving from position i to position j at time t is expressed as follows:

$p^k_{ij} = $


### Pseudo Code

```
  procedure ACO_MetaHeuristic
    while(not_termination)
       generateSolutions()
       daemonActions()
       pheromoneUpdate()
    end while
  end procedure

```



### Improvement

- Use greedy algorithm to initialize the ACO of TSP.

  Greedy algorithm is an algorithmic paradigm that follows the problem solving heuristic of making the locally optimal choice at each stage[1] with the hope of finding a global optimum. In many problems, a greedy strategy does not in general produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a global optimal solution in a reasonable time.
- Rotate the matrix of cities to avoid to fail into the local optimization.


### Result

![](http://oljkaeely.bkt.clouddn.com/static/image/Travelling-Salesman-Problem/aco_result_1000.jpg)



## PSO

A basic variant of the PSO algorithm works by having a population (called a swarm) of candidate solutions (called particles). These particles are moved around in the search-space according to a few simple formulae. 

The movements of the particles are guided by their own best known position in the search-space as well as the entire swarm's best known position. When improved positions are being discovered these will then come to guide the movements of the swarm. The process is repeated and by doing so it is hoped, but not guaranteed, that a satisfactory solution will eventually be discovered.

Formally, let f: ℝn → ℝ be the cost function which must be minimized. The function takes a candidate solution as argument in the form of a vector of real numbers and produces a real number as output which indicates the objective function value of the given candidate solution. The gradient of f is not known. The goal is to find a solution a for which f(a) ≤ f(b) for all b in the search-space, which would mean a is the global minimum. Maximization can be performed by considering the function h = -f instead.

Let S be the number of particles in the swarm, each having a position xi ∈ ℝn in the search-space and a velocity vi ∈ ℝn. Let pi be the best known position of particle i and let g be the best known position of the entire swarm. A basic PSO algorithm is then:

### Pseudo Code

```
for each particle i = 1, ..., S do
   Initialize the particle's position with a uniformly distributed random vector: xi ~ U(blo, bup)
   Initialize the particle's best known position to its initial position: pi ← xi
   if f(pi) < f(g) then
       update the swarm's best known  position: g ← pi
   Initialize the particle's velocity: vi ~ U(-|bup-blo|, |bup-blo|)
while a termination criterion is not met do:
   for each particle i = 1, ..., S do
      for each dimension d = 1, ..., n do
         Pick random numbers: rp, rg ~ U(0,1)
         Update the particle's velocity: vi,d ← ω vi,d + φp rp (pi,d-xi,d) + φg rg (gd-xi,d)
         Update the particle's position: xi ← xi + vi
         if f(xi) < f(pi) then
            Update the particle's best known position: pi ← xi
            if f(pi) < f(g) then
               Update the swarm's best known position: g ← pi
```

### Result

![](http://oljkaeely.bkt.clouddn.com/static/image/Travelling-Salesman-Problem/pso_result_1000.jpg)

### Conclusion
We can find that the PSO is the slowest descent to the result, and it cost too much time than others.



# Reference

https://en.wikipedia.org/wiki/Genetic_algorithm

https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms


https://en.wikipedia.org/wiki/Particle_swarm_optimization



# Appendix - Source Code in TSP
[github](https://github.com/Yvon-Shong/Waseda/tree/master/Computational_Intelligence/TSP)