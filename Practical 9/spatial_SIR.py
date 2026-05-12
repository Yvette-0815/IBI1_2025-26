# import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define variables of the model
size = 100 # Grid size (100 * 100)
beta = 0.3
gamma = 0.05
time_steps = 100

# Status: 0 = Suscepts, 1 = Infections, 2 = Recoveries
population = np.zeros((size, size), dtype=int)
# Randomly select initial outbreak point
outbreak = np.random.choice(range(size), 2) 
population[outbreak[0], outbreak[1]] = 1

def get_neighbors(x, y, size):
    # Handle boundariy cases
    neighbors = []
    for i in range(max(0, x-1), min(size, x+2)): # x - 1 to x + 1
        for j in range(max(0, y-1), min(size, y+2)): # y - 1 to y + 1
            if not (i == x and j == y):  # Exclude self
                neighbors.append((i, j))
    return neighbors

# Main simulation
for t in range(time_steps):
    # Create the grid for current time step
    new_population = population.copy()
    infected_positions = np.argwhere(population == 1)
    for ix, iy in infected_positions:
        neighbors = get_neighbors(ix, iy, size)
        for nx, ny in neighbors:
            # Only infect suscepts(0) neighbors
            if population[nx, ny] == 0:
                if np.random.rand() < beta:
                    new_population[nx, ny] = 1
        if np.random.rand() < gamma:
            new_population[ix, iy] = 2
            
    # Update the grid with the new state
    population = new_population
    
    if t % 10 == 0 or t == 1 or t == time_steps - 1:
        plt.figure(figsize=(6, 4), dpi=150)
        # Use viridis color mapping: Purple(0) = Suscepts, Bluegreen(1) = Infections, Yellow(2) = Recoveries
        plt.imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
        plt.colorbar(label='State (0=S, 1=I, 2=R)')
        plt.title(f'Spatial SIR Model at Time Step {t}')
        plt.axis('off')
        plt.show()
        
# Print final status statistics
unique, counts = np.unique(population, return_counts=True)
state_dict = dict(zip(unique, counts))
print("Simulation Finished!")
print(f"Final Counts - Susceptible: {state_dict.get(0, 0)}, Infected: {state_dict.get(1, 0)}, Recovered: {state_dict.get(2, 0)}")

input("Press enter to exit.")