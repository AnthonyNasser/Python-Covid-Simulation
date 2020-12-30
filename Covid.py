import numpy as np
from AdjacencyMatrix import AdjacencyMatrix
import matplotlib.pyplot as plt
import random

DEAD = 2
RECOVERED = 3
RECOVERY_DAYS = 14
CLEAN = 0
INFECTED = 1

INIT_SETTING = 0.01
DEATH_RATE = 0.03
TRANSMISSION_RATE = 0.015
ALPHA = 0.01

class CovidModel():
    def __init__(self, interaction: int, n: int):
        self.interaction = interaction
        self.day = 0
        self.accumulated_deaths = 0
        self.infected_data = []
        self.n = n

        self.states = self.new_zeros_array(self.n)
        self.recovers = self.new_zeros_array(self.n)

        for i in range(0, self.n):
            if random.random() < INIT_SETTING:
                self.states[i] = INFECTED
                self.recovers[i] = RECOVERY_DAYS

    def new_zeros_array(self, n):
        return np.zeros(n, dtype=int)

    def get_interaction_graph(self):
        g = AdjacencyMatrix(self.n)
        for time in range(0, self.interaction):
            for j in range(0, self.n):
                i = 0
                if j > 0:
                    i = random.randrange(0, j, 1)
                else:
                    i = random.randrange(1, self.n, 1)

                if random.random() < ALPHA:
                    g.add_edge(j, i)
                else:
                    node_i_points_to = g.out_edges(i)
                    if len(node_i_points_to) > 0:
                        k = random.choice(node_i_points_to)
                        g.add_edge(j, k)
        return g

    def simulation(self):
        deaths = 0
        infects = 0
        self.day = self.day + 1

        interaction_graph = self.get_interaction_graph()
        for v in range(0, self.n):
            if (self.states[v] == INFECTED):
                for w in interaction_graph.out_edges(v):
                    if (self.states[w] == CLEAN):
                        if (random.random() < TRANSMISSION_RATE):
                            self.states[w] = INFECTED
                            self.recovers[w] = RECOVERY_DAYS
                            infects = infects + 1

                self.recovers[v] = self.recovers[v] - 1

                if (self.recovers[v] == 0):
                    if (random.random() < DEATH_RATE):
                        self.states[v] = DEAD
                        deaths = deaths + 1
                    else:
                        self.states[v] = RECOVERED

        print("Day", self.day, "- Deaths:", deaths, "- Infects:", infects)

        self.accumulated_deaths = self.accumulated_deaths + deaths
        self.infected_data.append(infects)

LOCKDOWN = CovidModel(interaction=5, n=150)
NO_LOCKDOWN = CovidModel(interaction=60, n=150)

print("Lockdown simulation: ")
for i in range(30):
    LOCKDOWN.simulation()

print("")
print("No Lockdown simulation: ")
for i in range(30):
    NO_LOCKDOWN.simulation()


x_pos = range(1, 31)
fig, axes = plt.subplots(nrows=3, ncols=1)


infected_number = NO_LOCKDOWN.infected_data
plt.sca(axes[1])
plt.bar(x_pos, infected_number, color='green')
plt.xlabel("DAYS")
plt.ylabel("INFECTED PEOPLE")
plt.title("THE NUMBER OF INFECTED PEOPLE PER DAY IN LOCKDOWN")
plt.xticks(x_pos)
plt.xticks(rotation=90)
plt.yticks(rotation=90)

infected_number = NO_LOCKDOWN.infected_data
plt.sca(axes[1])
plt.bar(x_pos, infected_number, color='green')
plt.xlabel("DAYS")
plt.ylabel("INFECTED PEOPLE")
plt.title("THE NUMBER OF INFECTED PEOPLE PER DAY IN LOCKDOWN")
plt.xticks(x_pos)
plt.xticks(rotation=90)
plt.yticks(rotation=90)

plt.sca(axes[2])
lockdown_deaths = LOCKDOWN.accumulated_deaths
no_lockdown_deaths = NO_LOCKDOWN.accumulated_deaths
plt.bar(["LOCKDOWN", "NO LOCKDOWN"], [lockdown_deaths, no_lockdown_deaths], color='green')
plt.ylabel("DEAD PEOPLE")
plt.title("THE ACCUMULATED NUMBER OF DEAD PEOPLE")

plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.35)
fig.tight_layout()
plt.show()