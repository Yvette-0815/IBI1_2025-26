# import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm # Obtain rich color mappings

#  Define variables of the model
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

vaccination_rates = [i / 100 for i in range(0, 101, 10)]
plt.figure(figsize = (6, 4), dpi = 150)
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))
for idx, v_rate in enumerate(vaccination_rates): 
    V = int(N * v_rate) # Vaccinated population
    S = max(0, N - V - 1) # Avoid negative number
    I = 1
    R = 0
    I_list = [I]
    
    for t in range(time_steps):
        infected_fraction = I / N
        # Only generate new infections from S
        new_infections = np.random.choice([0, 1], S, p = [1 - beta * infected_fraction, beta * infected_fraction]).sum()
        new_recoveries = np.random.choice([0, 1], I, p = [1 - gamma, gamma]).sum()
        S -= new_infections
        I = I + new_infections - new_recoveries
        R += new_recoveries
        I_list.append(I)
    plt.plot(I_list, label = f'{int(v_rate * 100)}% vaccinated', color = colors[idx], linewidth=1.5)

plt.xlabel('Time Steps')
plt.ylabel('Number of Infected People')
plt.title('SIR Model: Effect of Vaccination on Infection Spread')
plt.legend(title = 'Vaccination Rate', bbox_to_anchor = (1.05, 1), loc = 'upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("SIR_vaccination_effect.png", dpi=300, bbox_inches='tight')
plt.show()

input("Press enter to exit.")