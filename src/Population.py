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

  def make_next_populaton(self, array):
    next_population = []
    for i in range(self.population_size):
      gene_array = []
      for j in range(self.individual_size):
        rand = np.random.random()
        gene_array.append('1' if rand<array[j] else '0')
      new_individual = Individual(self.individual_size)
      new_individual.clone(''.join(gene_array))
      next_population.append(new_individual)
    self.array = np.array(next_population)
    return self


if __name__ == '__main__':
  population_size = 6
  individual_size = 5

  population = Population(population_size, individual_size)
  population.sort_by_fitness()
  prob = np.mean(population.get_gene_array(3), axis=0)
  print(prob)
  # population.print_population()
  population.make_next_populaton(prob)
  # population.print_population()

