import numpy as np
from Individual import Individual

class Population:
  def __init__(self, population_size, individual_size):
    self.array = np.array([Individual(individual_size) for i in range(population_size)])
    self.individual_size = individual_size
    self.population_size = population_size

  def print_population(self):
    for i in range(len(self.array)):
      self.array[i].print_individual()

  def sort_by_fitness(self):
    self.array = sorted(self.array, key=lambda x: x.fitness)[::-1]

  def get_gene_array(self, n):
    return np.array([[int(i) for i in self.array[j].gene] for j in range(n)])

if __name__ == '__main__':
  population_size = 6
  individual_size = 5

  population = Population(population_size, individual_size)
  population.sort_by_fitness()
  print(np.mean(population.get_gene_array(3), axis=1))
  population.print_population()

