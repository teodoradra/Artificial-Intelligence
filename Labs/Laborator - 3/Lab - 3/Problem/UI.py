from Problem.HillClimbing.HC import *
from Problem.EA.EA import *
from matplotlib import pyplot as plt
import numpy as np
from Problem.PSO.PSO import *


class Console:
    def __init__(self):
        self.__algorithm = ""

    def run(self):
        self.__print_menu()
        while self.__algorithm:
            if self.__algorithm == "exit":
                exit(0)
            number_of_iteration = int(input("\tNumber of iteration: "))
            population_size = int(input("\tPopulation number (for EA): "))
            prob_of_mutation = float(input("\tProbability of mutation: "))
            input_set_s = input("Set S: ")
            input_set_s = input_set_s.split(",")
            set_s = []
            for e in input_set_s:
                set_s.append(int(e))
            input_set_t = input("Set T: ")
            input_set_t = input_set_t.split(",")
            set_t = []
            for e in input_set_t:
                set_t.append(int(e))
            best = []
            if self.__algorithm == "EA":
                for i in range(30):
                    ea = EA(number_of_iteration, prob_of_mutation, population_size, set_s, set_t)
                    ea.run()
                    best.append(ea.best().fitness())
                    print("\tThe best solution found: \n" + str(ea.best()) + "\nWith fitness: " + str(ea.best().fitness()))
                self.drawPlot(best)

            elif self.__algorithm == "HC":
                for _ in range(30):
                    hc = HillClimbing(number_of_iteration, prob_of_mutation, set_s, set_t)
                    hc.run()
                    best.append(hc.best())
                self.drawPlot(best)

            elif self.__algorithm == "PSO":
                for _ in range(30):
                    w = 1.0
                    c1 = 1.0
                    c2 = 2.5
                    nr_of_neighbours_per_particle = 20
                    pso = PSO(number_of_iteration, population_size, nr_of_neighbours_per_particle, w, c1, c2, set_s, set_t)
                    best.append(pso.run())
                self.drawPlot(best)
            else:
                print("Wrong command!")
            self.__print_menu()

    def drawPlot(self, values):
        arr = np.array(values)
        m = np.mean(arr, axis=0)
        std = np.std(arr, axis=0)
        means = []
        stddev = []
        for i in range(30):
            means.append(m)
            stddev.append(std)
        plt.plot(range(30), means)
        plt.plot(range(30), stddev)
        plt.plot(range(30), values)
        plt.show()

    def __print_menu(self):
        print("\t Algorithms: ")
        print("------- EA -------")
        print("------- Hill Climbing(HC) -------")
        print("------- PSO -------")
        print("------- exit -------")
        self.__algorithm = input("What algorithm? ")
