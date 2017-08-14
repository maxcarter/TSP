# Traveling Salesman Problem

The [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (TSP) is an NP-hard problem that asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?" ([Wikipedia](https://en.wikipedia.org/wiki/Travelling_salesman_problem)).


This repository is my solution to the TSP using various artificial intelligence search algorithms.


## Run
```
python run.py
```


## Search Algorithms

### Simulated Annealing

[Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing) is an algorithm based on the process of physical annealing. Physical annealing is a process used to strengthen metals and glass. It involves heating the material to a hot annealing temperature and slowly cooling it back down to normal temperature. If the material is cooled too quickly, the material becomes brittle. If the material does not cool enough it becomes flimsy. If the material is cooled too much, it freezes. The goal is to heat and cool it at the proper pace to ensure a strong and robust result.


Simulated annealing follows a similar process. The algorithm begins with an initial temperature and slowly reduces the temperature based on a thermal dynamics equation until a threshold temperature is achieved. During this processes, various solutions are accepted and rejected based on a probability function. As the temperature cools, the probability of selecting a better solution improves.


### Genetic Algorithm
[Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm) is a metaheuristic algorithm inspired by natural selection. In this algorithm, organisms are grouped into a population. The fittest few are selected as parents and used to create offspring. The offspring contain a crossover of both parent's genes, along with a random mutation. The offspring then participate in the next generation of organisms. The cycle continues until an organism of a certain fitness is obtained.
