# Agent-Based Model (ABM) to study collective behavior in ants
# This script converts an ODE model into an ABM to explore decision-making and resource allocation in ants.

import numpy as np
import matplotlib.pyplot as plt
import time

# Constants and parameters
GRID_SIZE = (50, 50)  # Size of the grid
NEST_LOCATION = (25, 5)  # Nest location in the grid
FEEDER_A_LOCATION = (10, 40)  # Location of Feeder A
FEEDER_B_LOCATION = (40, 40)  # Location of Feeder B
FOOD_UNITS = 100  # Initial food units at each feeder

# States
UNCOMMITTED = 'uncommitted'
COMMITTED_TO_A = 'committed to A'
COMMITTED_TO_B = 'committed to B'

# Probabilities and rates
ALPHA = 0.75  # Discovery rate for both feeders
BETA_A = 0.9  # Recruitment rate to feeder A
BETA_B = 0.36  # Recruitment rate to feeder B
LAMBDA_A = 0.009  # Attrition rate from feeder A
LAMBDA_B = 0.038  # Attrition rate from feeder B

# Initializing feeders with their properties
feeders = {
    'A': {'location': FEEDER_A_LOCATION, 'food': FOOD_UNITS, 'beta': BETA_A, 'lambda': LAMBDA_A},
    'B': {'location': FEEDER_B_LOCATION, 'food': FOOD_UNITS, 'beta': BETA_B, 'lambda': LAMBDA_B}
}

# Ant class definition
class Ant:
    def __init__(self):
        self.location = NEST_LOCATION  # Initial location of the ant
        self.state = UNCOMMITTED  # Initial state of the ant
        self.food_collected = 0  # Food collected by the ant

    def move(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if self.state == UNCOMMITTED:
            move = directions[np.random.choice(len(directions))]
            self.location = (self.location[0] + move[0], self.location[1] + move[1])
            self.location = (max(0, min(self.location[0], GRID_SIZE[0]-1)),
                             max(0, min(self.location[1], GRID_SIZE[1]-1)))
        else:
            self.directed_move(feeders[self.state.split()[-1]]['location'])
        self.interact()

    def interact(self):
        for other_ant in ants:
            if (self.location == other_ant.location) and (self.state != UNCOMMITTED and other_ant.state == UNCOMMITTED):
                distance = abs(other_ant.location[0] - self.location[0]) + abs(other_ant.location[1] - self.location[1])
                if distance <= 1 and np.random.random() < feeders[self.state.split()[-1]]['beta']:
                    other_ant.state = self.state

    def directed_move(self, target_location):
        x_move = np.sign(target_location[0] - self.location[0])
        y_move = np.sign(target_location[1] - self.location[1])
        self.location = (self.location[0] + x_move, self.location[1] + y_move)

    def update_state(self):
        for feeder_name, feeder_info in feeders.items():
            if self.location == feeder_info['location'] and np.random.random() < ALPHA:
                self.state = 'committed to ' + feeder_name

    def collect_food(self):
        if self.state.startswith('committed'):
            feeder_name = self.state.split()[-1]
            if self.location == feeders[feeder_name]['location'] and feeders[feeder_name]['food'] > 0:
                feeders[feeder_name]['food'] -= 1
                self.food_collected += 1
                self.location = NEST_LOCATION

    def recruitment(self):
        if self.location == NEST_LOCATION and self.state != UNCOMMITTED:
            for other_ant in ants:
                if other_ant.state == UNCOMMITTED:
                    if np.random.random() < feeders[self.state.split()[-1]]['beta']:
                        other_ant.state = self.state

    def attrition(self):
        if self.state != UNCOMMITTED and np.random.random() < feeders[self.state.split()[-1]]['lambda']:
            self.state = UNCOMMITTED

# Initializing ant colony
ants = [Ant() for _ in range(N)]

# Simulation function
def simulate(time_steps=500):
    start_time = time.time()
    ant_distribution_over_time = {'A': [], 'B': [], 'Uncommitted': []}
    
    for step in range(time_steps):
        ant_distribution = {'committed to A': 0, 'committed to B': 0, 'uncommitted': 0}
        
        for ant in ants:
            ant.move()
            ant.update_state()
            ant.collect_food()
            ant.recruitment()
            ant.attrition()
            ant_distribution[ant.state] += 1

        ant_distribution_over_time['A'].append(ant_distribution['committed to A'])
        ant_distribution_over_time['B'].append(ant_distribution['committed to B'])
        ant_distribution_over_time['Uncommitted'].append(ant_distribution['uncommitted'])

        if feeders['A']['food'] == 0 or feeders['B']['food'] == 0:
            depleted_feeder = [k for k, v in feeders.items() if v['food'] == 0][0]
            print(f"Feeder {depleted_feeder} depleted at step {step}")
            break

    end_time = time.time()
    print(f"Simulation ended. Total time elapsed: {end_time - start_time:.2f} seconds.")
    return ant_distribution_over_time

# Running the simulation
ant_distribution = simulate()

# Function for calculating moving averages
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Calculating moving averages for smoother plot lines
window_size = 50
smoothed_A = moving_average(ant_distribution['A'], window_size)
smoothed_B = moving_average(ant_distribution['B'], window_size)
smoothed_Uncommitted = moving_average(ant_distribution['Uncommitted'], window_size)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(smoothed_A, label='Feeder A (Smoothed)')
plt.plot(smoothed_B, label='Feeder B (Smoothed)')
plt.plot(smoothed_Uncommitted, label='Uncommitted (Smoothed)')
plt.legend()
plt.title('Ant Distribution Over Time with Two Feeders (Smoothed)')
plt.xlabel('Time Steps')
plt.ylabel('Number of Ants')
plt.show()
