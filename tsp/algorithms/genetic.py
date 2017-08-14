import signal
import copy
import random


class GeneticAlgorithm:
    user_exit = False

    def __init__(self, organism, distance_matrix, generations=1000, population_size=200, min_cost=42000, parents=4, children=200, elite=0, mutation_rate=0.3, verbose=False):
        self.organism = copy.copy(organism)
        self.distance_matrix = distance_matrix
        self.generations = generations
        self.population_size = population_size
        self.min_cost = min_cost
        self.parents = parents
        self.children = children
        self.elite = elite
        self.mutation_rate = mutation_rate
        self.verbose = verbose
        signal.signal(signal.SIGINT, self.set_exit)

    def set_exit(self, signum, frame):
        self.user_exit = True

    def calculate_cost(self, organism):
        cost = 0
        for i in range(len(organism)):
            cost += self.distance_matrix[organism[i - 1]][organism[i]]
        return cost

    def getKey(self, item):
        return item[1]

    def score_population(self, population):
        scored_population = []
        for i in range(len(population)):
            organism = copy.copy(population[i])
            cost = self.calculate_cost(organism)
            scored_population.append((organism, cost))
        scored_population = sorted(scored_population, key=self.getKey)
        return scored_population

    def mutate(self, organism):
        a = random.randint(0, len(organism) - 1)
        b = random.randint(0, len(organism) - 1)
        organism[a], organism[b] = organism[b], organism[a]
        return organism

    def generate_population(self):
        population = []
        for i in range(self.population_size):
            population.append(self.mutate(self.organism))
        return population

    def crossover(self, parent1, parent2):
        child = []

        for i in range(len(parent1)):
            child.append('x')

        start = random.randint(0, len(child) - 1)
        end = random.randint(0, len(child) - 1)

        if start > end:
            start, end = end, start

        count = start
        while count != end:
            child[count] = parent1[count]
            count += 1

        for j in range(len(parent2)):
            if parent2[j] not in child:
                for k in range(len(child)):
                    if child[k] == 'x':
                        child[k] = parent2[j]
                        break

        if random.randint(0, 1) < self.mutation_rate:
            child = self.mutate(child)

        return child

    def simulate(self):
        generation = 0
        population = self.generate_population()
        while generation <= self.generations:

            print 'Generation: ', generation

            scored_population = self.score_population(population)
            if self.user_exit or scored_population[0][1] < self.min_cost or generation == self.generations:
                return scored_population[0][0], scored_population[0][1]

            parents = []
            for j in range(self.parents):
                parents.append(scored_population[j][0])
            population = parents[0:self.elite]

            print 'Best cost: ', scored_population[0][1]

            for i in range(self.children):
                if self.user_exit:
                    break
                a = random.randint(0, self.parents - 1)
                b = random.randint(0, self.parents - 1)

                if a == b and a < len(parents) - 1:
                    a += 1
                elif a == b:
                    a -= 1

                parent1 = parents[a]
                parent2 = parents[b]

                child = self.crossover(parent1, parent2)
                population.append(child)

            generation += 1
