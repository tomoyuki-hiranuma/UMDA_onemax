import numpy as np
from Population import Population
import copy

class Umda:
  def __init__(self, tau, population_size, individual_size):
    self.tau = tau
    self.population = Population(population_size, individual_size)
    self.probability_array = self.make_probability()

  def make_probability(self):
    self.population.sort_by_fitness()
    selected_population = np.array(copy.deepcopy(self.population.get_gene_array(int(len(self.population.array)*self.tau))))
    return np.mean(selected_population, axis=0)


if __name__ == '__main__':
  TAU = 0.5
  POPULATION_SIZE = 6
  INDIVIDUAL_SIZE = 5

  umda = Umda(TAU, POPULATION_SIZE, INDIVIDUAL_SIZE)
  print(umda.probability_array)
