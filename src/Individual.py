import numpy as np

class Individual:
  def __init__(self, individual_size):
    self.gene = f'{np.random.randint(2**individual_size):0{individual_size}b}'
    self.fitness = sum([int(i) for i in self.gene])
    self.individual_size = individual_size

  def evaluation(self):
    self.fitness = sum([int(i) for i in self.gene])

  def print_individual(self):
    print("gene: {}, fitness: {}".format(self.gene, self.fitness))


if __name__ == '__main__':
  ind_length = 5
  ind1 = Individual(ind_length)
  print(ind1.gene)
  print(ind1.fitness)
  