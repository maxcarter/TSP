from tsp import Cities
from tsp import SimulatedAnnealing

if __name__ == '__main__':
    print 'Travleing Salesman Problem'
    print 'Please select an algorithm:'
    print '1 - Simulated Annealing'

    selection = raw_input('Selection: ')

    if selection == '1':
        cities = Cities()
        sa = SimulatedAnnealing(cities.generate_random_state(), cities.generate_distance_matrix())
        state, distance = sa.anneal()
        print state
        print distance
