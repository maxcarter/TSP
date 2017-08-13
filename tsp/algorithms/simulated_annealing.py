import signal
import math
import random
import copy

# This code is based on [Simanneal](https://github.com/perrygeo/simanneal)
class SimulatedAnnealing:
    verbose = False
    user_exit = False

    def __init__(self, init_state, distance_matrix, steps=50000, temp_max=25000.0, temp_min=2.5, verbose=False):
        self.state = copy.copy(init_state)
        self.distance_matrix = distance_matrix
        self.steps = steps
        self.tempurature_max = temp_max
        self.tempurature_min = temp_min
        self.cooling_factor = self.calculate_cooling_factor()
        self.verbose = verbose
        signal.signal(signal.SIGINT, self.set_exit)

    def set_exit(self, signum, frame):
        self.user_exit = True

    def calculate_cost(self):
        cost = 0
        for i in range(len(self.state)):
            cost += self.distance_matrix[self.state[i - 1]][self.state[i]]
        return cost

    def calculate_cooling_factor(self):
        return -math.log(self.tempurature_max / self.tempurature_min)

    def exponential_cool(self, step):
        return self.tempurature_max * math.exp(self.cooling_factor * step / self.steps)

    def change_state(self):
        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

    def anneal(self):
        temperature = self.tempurature_max

        cost = self.calculate_cost()
        previous_cost = cost
        best_cost = cost

        previous_state = copy.copy(self.state)
        best_state = copy.copy(self.state)

        trials = 0
        step = 0

        while step < self.steps:
            if self.user_exit:
                break

            step += 1
            temperature = self.exponential_cool(step)
            self.change_state()
            cost = self.calculate_cost()

            delta_cost = cost - previous_cost

            if self.verbose:
                print 'Step: ', step
                print 'Temperature: ', temperature
                print 'Cost: ', cost
                print 'Previous Cost: ', previous_cost
                print 'Delta Cost: ', delta_cost

            if delta_cost < 0.0:
                # Accept new state
                if self.verbose:
                    print 'Cost is Improving'
                    print '-> Accept new state'
                previous_state = copy.copy(self.state)
                previous_cost = cost

                if cost < best_cost:
                    best_state = copy.copy(self.state)
                    best_cost = cost
            else:
                random_number = random.random()
                thermal_number = math.exp(-cost / temperature)
                if self.verbose:
                    print 'Random Number: ', random_number
                    print 'Thermal Number: ', thermal_number
                if thermal_number < random_number:
                    # Keep previous state
                    if self.verbose:
                        print '-> Keep previous state'
                    self.state = copy.copy(previous_state)
                    cost = previous_cost
                else:
                    # Accept new state
                    if self.verbose:
                        print '-> Accept new state'
                    previous_state = copy.copy(self.state)
                    previous_cost = cost

                    if cost < best_cost:
                        best_state = copy.copy(self.state)
                        best_cost = cost
        return best_state, best_cost
