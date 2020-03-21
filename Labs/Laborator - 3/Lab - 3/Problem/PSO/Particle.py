from itertools import permutations
from random import randint


class Particle:
    def __init__(self, list_of_values_s, list_of_values_t):
        self.__position = self.__generate_individual(list_of_values_s, list_of_values_t)
        self.__position_size = len(list_of_values_s)
        self.__s = list_of_values_s
        self.__t = list_of_values_t
        self.__fitness = self.fit(self.__position)
        self.__velocity = [0 for _ in range(self.__position_size)]

        # the memory of that particle
        self.__best_position = self.__position.copy()
        self.__best_fitness = self.__fitness

    def __generate_individual(self, list_of_values_s, list_of_values_t):
        permute_s = list(permutations(list_of_values_s))
        permute_t = list(permutations(list_of_values_t))
        ind = []
        for i in range(len(list_of_values_s)):
            pos_in_permute_s = randint(0, len(permute_s)-1)
            pos_in_permute_t = randint(0, len(permute_s)-1)
            ind.append(self.__transform_two_list(permute_s[pos_in_permute_s], permute_t[pos_in_permute_t]))
        return ind

    def __transform_two_list(self, list_s, list_t):
        ls = []
        for i in range(len(list_s)):
            tup = (list_s[i], list_t[i])
            ls.append(tup)
        return ls

    def __str__(self):
        return str(self.__position)

    def fit(self, position):
        n = len(position)
        f = 0
        for i in range(n):
            f += self.__cost(i, 0)
        for i in range(n):
            f += self.__cost(i, 1)
        return f

    def __cost(self, pos, first_or_second):
        s = 0
        ls_s = {}
        for i in range(self.__position_size):
            if self.__position[i][pos][first_or_second] in ls_s.keys():
                ls_s[self.__position[i][pos][first_or_second]] = ls_s.get(self.__position[i][pos][first_or_second]) + 1
                s += 1
            else:
                ls_s[self.__position[i][pos][first_or_second]] = 1
        return s

    def evaluate(self):
        self.__fitness = self.fit(self.__position)

    @property
    def position(self):
        return self.__position

    @property
    def fitness(self):
        return self.__fitness

    @property
    def best_position(self):
        return self.__best_position

    @property
    def best_fitness(self):
        return self.__best_fitness

    @property
    def velocity(self):
        return self.__velocity

    @position.setter
    def position(self, new_position):
        self.__position = new_position.copy()
        self.evaluate()
        if self.fitness < self.__best_fitness:
            self.__best_position = self.__position
            self.__best_fitness = self.__fitness
