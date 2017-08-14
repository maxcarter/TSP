from tsp import Cities
from tsp import SimulatedAnnealing
from tsp import GeneticAlgorithm

if __name__ == '__main__':
    print 'Travleing Salesman Problem'
    print 'Please select an algorithm:'
    print '1 - Simulated Annealing'
    print '2 - Genetic Algorithm'

    selection = raw_input('Selection: ')

    cities = Cities()

    if selection == '1':
        sa = SimulatedAnnealing(cities.generate_random_state(), cities.generate_distance_matrix())
        state, distance = sa.anneal()
        print state
        print distance
    elif selection == '2':
        ga = GeneticAlgorithm(cities.generate_random_state(), cities.generate_distance_matrix())
        tour, distance = ga.simulate()
        print tour
        print distance
