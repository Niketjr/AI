import math
import random

def evaluate(state):
    return state ** 2

def generate_neighbor(current_state):
    return current_state + random.uniform(-1, 1)

def simulated_annealing(initial_state, initial_temperature, cooling_rate, max_iterations):
    current_state = initial_state
    current_energy = evaluate(current_state)
    best_state = current_state
    best_energy = current_energy
    temperature = initial_temperature

    while temperature > 0.1:  
        for iteration in range(max_iterations):
            new_state = generate_neighbor(current_state)
            new_energy = evaluate(new_state)
            energy_difference = new_energy - current_energy

            if energy_difference < 0:
                current_state = new_state
                current_energy = new_energy

                if current_energy < best_energy:
                    best_state = current_state
                    best_energy = current_energy
            else:
                acceptance_probability = math.exp(-energy_difference / temperature)
                if random.random() < acceptance_probability:
                    current_state = new_state
                    current_energy = new_energy

        temperature *= cooling_rate

    return best_state, best_energy

initial_state = 10  
initial_temperature = 1000 
cooling_rate = 0.99 
max_iterations = 100  

best_state, best_energy = simulated_annealing(initial_state, initial_temperature, cooling_rate, max_iterations)

print(f"Best State: {best_state}, Best Energy: {best_energy}")
