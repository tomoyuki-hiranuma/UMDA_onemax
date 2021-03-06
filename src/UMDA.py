import numpy as np
from Population import Population
import copy
import matplotlib.pyplot as plt

class Umda:
  def __init__(self, tau, population_size, individual_size):
    self.tau = tau
    self.population = Population(population_size, individual_size)
    self.probability_array = self.make_probability()

  def make_probability(self):
    self.population.sort_by_fitness()
    selected_population = np.array(copy.deepcopy(self.population.get_gene_array(int(len(self.population.array)*self.tau))))
    return np.mean(selected_population, axis=0)

  def make_offspring(self):
    offspring = Population(len(self.population.array), len(self.population.array[0].gene))
    return offspring.make_next_populaton(self.probability_array)

  def do_one_generation(self):
    self.population = self.make_offspring()
    self.probability_array = self.make_probability()


if __name__ == '__main__':
  TAU = 0.5
  POPULATION_SIZE = 100
  INDIVIDUAL_SIZE = 50
  MAX_GENERATION = 50

  vector_entries = []
  steps = []
  umda = Umda(TAU, POPULATION_SIZE, INDIVIDUAL_SIZE)
  vector_entries.append(umda.probability_array)
  steps.append(0)
  print("第{}世代".format(0))
  umda.population.print_population()
  for i in range(MAX_GENERATION):
    print("第{}世代".format(i+1))
    umda.do_one_generation()
    umda.population.print_population()
    vector_entries.append(umda.probability_array)
    steps.append(i+1)

  plt.plot(steps, vector_entries, color="blue")
  plt.ylim(0, 1.1)
  plt.xlim(0, MAX_GENERATION)
  plt.xlabel("generation")
  plt.ylabel("probability vector entries")
  plt.title("probability vector entries in each generation")
  plt.savefig("./png/UMDA_N={}_n={}_tau={}.png".format(POPULATION_SIZE, INDIVIDUAL_SIZE, TAU))
  # plt.show()




