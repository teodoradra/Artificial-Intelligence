from itertools import permutations
import random


class Individual:
    def __init__(self, prob_mutation, list_of_values_s, list_of_values_t):
        self.__individual = self.__generate_individual(list_of_values_s, list_of_values_t)
        self.__individual_size = len(list_of_values_s)
        self.__prob_mutation = prob_mutation
        self.__s = list_of_values_s
        self.__t = list_of_values_t


    def __generate_individual(self, list_of_values_s, list_of_values_t):
        permute_s = list(permutations(list_of_values_s))
        permute_t = list(permutations(list_of_values_t))
        ind = []
        for i in range(len(list_of_values_s)):
            pos_in_permute_s = random.randint(0, len(permute_s)-1)
            pos_in_permute_t = random.randint(0, len(permute_s)-1)
            ind.append(self.__transform_two_list(permute_s[pos_in_permute_s], permute_t[pos_in_permute_t]))
        return ind

    def __transform_two_list(self, list_s, list_t):
        ls = []
        for i in range(len(list_s)):
            tup = (list_s[i], list_t[i])
            ls.append(tup)
        return ls

    def __str__(self):
        return str(self.__individual)

    def fitness(self):
        f = 0
        for i in range(self.__individual_size):
            f += self.__cost(i, 0)
        for i in range(self.__individual_size):
            f += self.__cost(i, 1)
        return f

    def __cost(self, pos, first_or_second):
        s = 0
        ls_s = {}
        for i in range(self.__individual_size):
            if self.__individual[i][pos][first_or_second] in ls_s.keys():
                ls_s[self.__individual[i][pos][first_or_second]] = ls_s.get(self.__individual[i][pos][first_or_second]) + 1
                s += 1
            else:
                ls_s[self.__individual[i][pos][first_or_second]] = 1
        return s

    def mutation(self):
        for i in range(self.__individual_size - 1):
            if random.uniform(0, 1) < self.__prob_mutation:
                col_on = random.randint(0, self.__individual_size - 1)
                col_with = random.randint(0, self.__individual_size - 1)
                while col_on == col_with:
                    col_with = random.randint(0, self.__individual_size - 1)
                aux = self.__individual[i][col_on]
                self.__individual[i][col_on] = self.__individual[i][col_with]
                self.__individual[i][col_with] = aux

    def crossover(self, p1, p2):
        n = p1.__get_size()
        c1 = random.randint(0, n - 1)
        c2 = random.randint(c1 + 1, n)
        for i in range(0, n):
            if i >= c1 and i < c2:
                self.__individual[i] = p1.get_value(i)
            else:
                self.__individual[i] = p2.get_value(i)

    def __lt__(self, other):
        return self.fitness() < other.fitness()

    def __get_size(self):
        return self.__individual_size

    def get_value(self, i):
        return self.__individual[i]

    def get_pair(self, i, j):
        return self.__individual[i][j]

    def interchange_pairs(self, pair, i, j):
        self.__individual[i][j] = pair
