# import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the initial variables of the model
N = 10000 # Total population
S = 9999 # Initial suscepts
I = 1 # Initial infections
R = 0 # Initial recoveries

beta = 0.3 # Contact infection probability
gamma = 0.05 # Recovery probability

# Create array to record the state at each time step
S_list = [S]
I_list = [I]
R_list = [R]

# Simulate 1000 time steps
time_steps = 1000
for t in range(time_steps):
    # Calculate the proportion of current infected people
    infection_fraction = I / N
    # Probability of each suscept being infected is beta * infection proportion
    new_infections = np.random.choice([0,1],S,p = [1 - beta * infection_fraction,beta * infection_fraction]).sum()
    # Probability of each infection recovering is gamma
    new_recoveries = np.random.choice([0,1],I,p = [1 - gamma,gamma]).sum()
    # Update population
    S -= new_infections
    I = I + new_infections - new_recoveries
    R += new_recoveries
    # Record in the list
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

plt.figure(figsize = (6, 4), dpi = 100)
plt.plot(S_list, label = 'Susceptible People', color = 'skyblue')
plt.plot(I_list, label = 'Infected People', color = 'lightcoral')
plt.plot(R_list, label = 'Recovered People', color = 'mediumspringgreen')
plt.xlabel('Time Steps')
plt.ylabel('Population')
plt.title('SIR Model Simulation (Probabilistic)')
plt.legend()
plt.grid(True, alpha = 0.3)

plt.savefig("SIR_simulation.png", dpi = 300, bbox_inches = 'tight')
plt.show()

input("Press enter to exit.")