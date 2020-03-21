# -*- coding: utf-8 -*-
"""

jumping frogs:
    find a sequence of valid steps in order to swich places of n red frogs with
    n brown frogs.

    A step is valid if a frog moves a step forward or jumps over one frog
    if the destination place is empty

    Red frogs are moving only in the direction from the begining to the end
    of the line brown frogs are moving only in the direction from the end of
    the line towards the begining

    example:
    initial configuration: RRR BBB
    final configuration: BBB RRR


    we observe running this example that the BestFS takes a longer time for n=10
    than BFS (over more 50 times longer) due the fact that the heuristic leads
    to 'dead paths' also computing the heuristic and sorting the new vertexes
    consume computing power

    """

from time import time


class Configuration:
    '''
    holds a configurations of frogs
    '''

    def __init__(self, positions):
        self.__size = len(positions)
        self.__values = positions[:]
        self.__cnt = 0

    def getSize(self):
        return self.__size

    def getValues(self):
        return self.__values[:]

    def nextConfig(self, j):
        '''
        moves the frog from the position j in the proper next position(s)
        in: the position of the moving frog j
        out: the list of the next correct configurations obtained moving this frog
        '''

        if j >= 0 and j < self.__size:
            self.__values[j] = j
            self.__cnt += 1
        return self.__values

    def isGoal(self):
        if self.__size == self.__cnt:
            return True
        else:
            return False

    def unPlace(self):
        if self.__cnt > 0:
            self.__cnt -= 1

    def isSafe(self,j):
        for i in range(self.__cnt):
            if self.__values[i] == j or abs(j-self.__values[i] == j-i):
                return False
            return True


    def __eq__(self, other):
        if not isinstance(other, Configuration):
            return False
        if self.__size != other.getSize():
            return False
        for i in range(self.__size):
            if self.__values[i] != other.getValues()[i]:
                return False
        return True

    def __str__(self):
        return str(self.__values)


class State:
    '''
    holds a PATH of configurations
    '''

    def __init__(self):
        self.__values = []

    def setValues(self, values):
        self.__values = values[:]

    def getValues(self):
        return self.__values[:]

    def __str__(self):
        s = ''
        for x in self.__values:
            s += str(x) + "\n"
        return s

    def __add__(self, something):
        aux = State()
        if isinstance(something, State):
            aux.setValues(self.__values + something.getValues())
        elif isinstance(something, Configuration):
            aux.setValues(self.__values + [something])
        else:
            aux.setValues(self.__values)
        return aux


class Problem:

    def __init__(self, initial, final):
        self.__initialConfig = initial
        self.__finalConfig = final
        self.__initialState = State()
        self.__initialState.setValues([self.__initialConfig])

    def expand(self, currentState):
        myList = []
        currentConfig = currentState.getValues()[-1]
        for j in range(currentConfig.getSize()):
            for x in currentConfig.nextConfig(j):
                myList.append(currentState + x)

        return myList

    def getFinal(self):
        return self.__finalConfig

    def getRoot(self):
        return self.__initialConfig

    def heuristics(self, state, finalC):
        l = finalC.getSize()
        count = 2 * l
        for i in range(l):
            if state.getValues()[-1].getValues()[i] != finalC.getValues()[i]:
                count = count - 1
        return count


class Controller:

    def __init__(self, problem):
        self.__problem = problem

    def DFS(self, root):

        if root.isGoal() == True:
            return root
        else:
            print(root.getSize())
            for i in range(root.getSize()):
                if root.isSafe(i):
                    root.nextConfig(i)
                    res = self.DFS(root)
                    if res != None:
                        return res
                    root.unPlace()

        return None

    def BestFS(self, root):
        return None


class UI:

    def __init__(self):
        self.__iniC = Configuration([0]*4)
        self.__finC = Configuration([0]*4)
        self.__p = Problem(self.__iniC, self.__finC)
        self.__contr = Controller(self.__p)

    def printMainMenu(self):
        s = ''
        s += "[RRR BBB] and [BBB RRR] are the default initial and final config.\n"
        s += "0 - exit \n"
        s += "1 - read the number of frogs \n"
        s += "2 - find a path with BFS \n"
        s += "3 - find a path with BestFS\n"
        print(s)

    def readConfigSubMenu(self):
        n = 4
        try:
            print("Input the number of red frogs (implicit n=4)")
            n = int(input("n = "))
        except:
            print("invalid number, the implicit value is still 4")
            n = 4
        self.__iniC = Configuration([0] * n)
        self.__finC = Configuration([0] * n)
        self.__p = Problem(self.__iniC, self.__finC)
        self.__contr = Controller(self.__p)

    def findPathBFS(self):
        startClock = time()
        print(str(self.__contr.DFS(self.__p.getRoot())))
        print('execution time = ', time() - startClock, " seconds")

    def findPathBestFS(self):
        startClock = time()
        print(str(self.__contr.BestFS(self.__p.getRoot())))
        print('execution time = ', time() - startClock, " seconds")

    def run(self):
        runM = True
        self.printMainMenu()
        while runM:
            try:
                command = int(input(">>"))
                if command == 0:
                    runM = False
                elif command == 1:
                    self.readConfigSubMenu()
                elif command == 2:
                    self.findPathBFS()
                elif command == 3:

                    self.findPathBestFS()
            except:
                print('invalid command')



def main():
    ui = UI()
    ui.run()


main()



