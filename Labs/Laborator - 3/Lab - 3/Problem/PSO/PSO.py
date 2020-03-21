from Problem.PSO.Population import *


class PSO:
    def __init__(self, no_of_iterations, population_dim, nr_of_neighbours_per_particle, w, c1, c2, list_s, list_t):
        self.__population = Population(population_dim, nr_of_neighbours_per_particle, c1, c2, list_s, list_t)
        self.__nr_of_iterations = no_of_iterations
        self.__crt_iter = 0
        self.__w = w
        self.__population_dim = population_dim

    def run(self):
        for i in range(self.__nr_of_iterations):
            self.__population.iteration(self.__w / (i + 1))

        best = 0
        for i in range(1, self.__population_dim):
            if self.__population.get_particle(i).fitness < self.__population.get_particle(best).fitness:
                best = i

        fitness_optim = self.__population.get_particle(best).fitness
        individual_optim = self.__population.get_particle(best).position
        print("The best matrix is:" + str(individual_optim) + "\n WIth fitness: " + str(fitness_optim))
        return fitness_optim

    def stop_condition(self):
        return self.__crt_iter == self.__nr_of_iterations
