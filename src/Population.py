import numpy as np
from Individual import Individual

class Population:
  def __init__(self, population_size, individual_size):
    self.array = np.array([Individual(individual_size) for i in range(population_size)])
    self.individual_size = individual_size

  def print_population(self):
    for i in range(len(self.array)):
      self.array[i].print_individual()

if __name__ == '__main__':
  population_size = 6
  individual_size = 5

  population = Population(population_size, individual_size)
  population.print_population()

