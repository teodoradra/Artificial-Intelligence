from Problem.EA.Population import *


class EA:
    def __init__(self, number_of_iter,  prob_mutation, population_size, list_s, list_t):
        self.__population = Population(population_size, prob_mutation, list_s, list_t)
        self.__population_size = population_size
        self.__list_s = list_s
        self.__list_t = list_t
        self.__individual_dimension = len(self.__list_t)
        self.__number_of_iteration = number_of_iter
        self.__crtIer = 0

    def run(self):
        while not self.stop_condition():
            print("Iteration " + str(self.__crtIer))
            self.__population.evaluate()
            self.__crtIer += 1

    def stop_condition(self):
        return self.__crtIer == self.__number_of_iteration or self.__population.best().fitness() == 0

    def best(self):
        return self.__population.best()