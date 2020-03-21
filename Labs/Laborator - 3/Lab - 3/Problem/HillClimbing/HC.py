from Problem.HillClimbing.Individual import *
import copy


class HillClimbing:
    def __init__(self, number_of_iter,  prob_mutation, list_s, list_t):
        self.__list_s = list_s
        self.__list_t = list_t
        self.__individual_dimension = len(self.__list_t)
        self.__number_of_iteration = number_of_iter
        self.__crtIer = 0
        self._possible_values = []
        self.__individual = Individual(prob_mutation, list_s, list_t)
        self.__best_solution = copy.deepcopy(self.__individual)

    def evaluate(self):
        self.__mutate()

    def __mutate(self):
        col = 0
        row = 0
        for k in range(self.__individual_dimension):
            for i in range(self.__individual_dimension):
                for j in range(self.__individual_dimension):
                    if col != j or row != i:
                        aux = self.__individual.get_pair(row, col)
                        self.__individual.interchange_pairs(self.__best_solution.get_pair(i, j), row, col)
                        self.__individual.interchange_pairs(aux, i, j)
                        if self.__individual.fitness() < self.__best_solution.fitness():
                            self.__best_solution = self.__individual
                            return
                        else:
                            self.__individual = self.__best_solution
                if col == self.__individual_dimension - 1:
                    col = 0
                else:
                    col += 1
            if row == self.__individual_dimension - 1:
                row = 0
            else:
                row += 1
        self.__individual = self.__best_solution

    def run(self):
        while not self.stop_condition():
            print("Iteration " + str(self.__crtIer))
            self.evaluate()
            self.__crtIer += 1

    def stop_condition(self):
        return self.__crtIer == self.__number_of_iteration or self.__best_solution.fitness() == 0

    def best(self):
        return self.__best_solution.fitness()
