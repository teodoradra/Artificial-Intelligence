from Problem.PSO.Particle import *
from random import random

class Population:
    def __init__(self, population_dim, nr_of_neighbours_per_particle, c1, c2, list_s, list_t):
        self.__population_dimension = population_dim
        self.__population = [Particle(list_s, list_t) for _ in range(population_dim)]
        self.__neighbours_per_particle_size = nr_of_neighbours_per_particle
        self.__neighbours = []
        self.__c1 = c1
        self.__c2 = c2
        self.select_neighbours()

    def select_neighbours(self):
        if self.__neighbours_per_particle_size > self.__population_dimension:
            self.__neighbours_per_particle_size = self.__population_dimension

        for i in range(self.__population_dimension):
            local_neighbour = []
            for j in range(self.__neighbours_per_particle_size):
                x = randint(0, self.__population_dimension - 1)
                while x in local_neighbour:
                    x = randint(0, self.__population_dimension - 1)
                local_neighbour.append(x)
            self.__neighbours.append(local_neighbour.copy())

    def iteration(self, w):
        best_neighbour = []
        for i in range(self.__population_dimension):
            best_neighbour.append(self.__neighbours[i][0])
            for j in range(1, len(self.__neighbours[i])):
                if self.__population[best_neighbour[i]].fitness > self.__population[self.__neighbours[i][j]].fitness:
                    best_neighbour[i] = self.__neighbours[i][j]
        self.update_velocity(best_neighbour, w)
        self.update_position(best_neighbour)

    def update_velocity(self, best_neighbours, w):
        for i in range(self.__population_dimension):
            for j in range(len(self.__population[0].velocity)):
                new_velocity = w * self.__population[i].velocity[j]
                new_velocity = new_velocity + self.__c1 * random() * (self.__compare_two_lists(self.__population[best_neighbours[i]].position[j], self.__population[i].position[j]))
                new_velocity = new_velocity + self.__c2 * random() * (self.__compare_two_lists(self.__population[i].best_position[j], self.__population[i].position[j]))
                self.__population[i].velocity[j] = new_velocity

    def update_position(self, best_neighbours):
        for i in range(self.__population_dimension):
            new_position = []
            for j in range(len(self.__population[0].velocity)):
                new_position.append(self.__population[best_neighbours[i]].position[j])
            self.__population[i].position = new_position

    def get_particle(self, i):
        return self.__population[i]

    def __compare_two_lists(self, l1, l2):
        c = 0
        for i in range(len(l1)):
            if l1[i] == l2[i]:
                c += 1
        return c