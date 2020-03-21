from Problem.HillClimbing.Individual import *


class Population:
    def __init__(self, population_size, prob_mutation, list_s, list_t):
        self.__prob_mutation = prob_mutation
        self.__list_s = list_s
        self.__list_t = list_t
        self.__population_size = population_size
        self.__population = self.__generate_population()

    def __generate_population(self):
        return [Individual(self.__prob_mutation, self.__list_s, self.__list_t) for i in range(self.__population_size)]

    def __str__(self):
        s = ""
        for i in self.__population:
            s += str(i)
            s += "\n"
        return s

    def best(self):
        return sorted(self.__population)[0]

    def evaluate(self):
        i1, i2 = self.__crossover_population()
        self.__mutation(i1, i2)
        self.exchange(i1, i2)

    def get_individual(self, pos):
        return self.__population[pos]

    def __crossover_population(self):
        i1 = random.randint(0, self.__population_size - 1)
        i2 = random.randint(0, self.__population_size - 1)
        return i1, i2

    def exchange(self, i1, i2):
        if i1 != i2:
            parent1 = self.__population[i1]
            parent2 = self.__population[i2]
            child = Individual(self.__prob_mutation, self.__list_s, self.__list_t)
            child.crossover(parent1, parent2)
            if parent1.fitness() > parent2.fitness() and parent1.fitness() > child.fitness():
                self.__population[i1] = child
            if parent2.fitness() > parent1.fitness() and parent2.fitness() > child.fitness():
                self.__population[i2] = child

    def __mutation(self, i1, i2):
        # for i in range(self.__population_size):
        #     if random.random() < self.__prob_mutation:
        self.__population[i1].mutation()
        self.__population[i2].mutation()