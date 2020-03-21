from time import time

class Configuration:
    def __init__(self,list):
        self.__values = list
        self.__size = len(list)
        self.__cnt = 0

    def getConfigSize(self):
        return self.__size

    def getConfigValues(self):
        return self.__values

    def isAFullConfig(self):
        zeros = 0
        for i in self.__values:
            if i == -1:
                zeros += 1
        return zeros == 0

    def nextConfig(self,j):
        if j >= 0 and j < self.__size:
            self.__values[self.__cnt] = j
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
            if self.__values[i] == j or abs(j-self.__values[i]) == self.__cnt-i:
                return False
        return True

    def __str__(self):
        return str(self.__values)


class State:
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
    def __init__(self,initial):
        self.__initialConfig = initial
        self.__initialState = State()
        self.__initialState.setValues([initial])

    def expand(self, currentState):
        myList = []
        currentConfig = currentState.getValues()[-1]
        for j in range(currentConfig.getSize()):
            for x in currentConfig.nextConfig(j):
                myList.append(currentState + x)
        return myList

    def getRoot(self):
        return self.__initialConfig

    def heuristic(self):
        #...
        return None


class Controller:

    def __init__(self, problem):
        self.__problem = problem

    def DFS(self,root,n):
        if root.isGoal() == True:
            return root
        else:
            for i in range(0,n):
                if root.isSafe(i):
                    root.nextConfig(i)
                    res = self.DFS(root,n)
                    if res != None:
                        return res
                    root.unPlace()

        return None

    def greedy(self,root,n):
        if root.isGoal() == True:
            return root
        else:
            for i in range(0,n):
                root.nextConfig(i)
                res = self.DFS(root,n)
                if res != None:
                    return res
                root.unPlace()
        return None


class UI:
    def __init__(self):
        self.__iniC = Configuration([-1]*4)
        self.__p = Problem(self.__iniC)
        self.__contr = Controller(self.__p)
        self.__n = 0

    def printMainMenu(self):
        s = ''
        s += "0 - exit \n"
        s += "2 - find a path with DFS \n"
        s += "3 - find a path with GREEDY\n"
        print(s)

    def readConfigSubMenu(self):
        print("Input the number")
        n = int(input("n = "))

        self.__iniC = Configuration([-1] * n)
        self.__p = Problem(self.__iniC)
        self.__contr = Controller(self.__p)
        self.__n = n

    def tansformMtx(self,mtr):
        m = [[0]* self.__n * self.__n]
        for i in range (self.__n):
            m[i,mtr[i]] = 1
        return m

    def findPathBFS(self):
        res = (str(self.__contr.DFS(self.__p.getRoot(),self.__n)))
        print(res)
        print(self.tansformMtx(res))

    def findPathBestFS(self):
        print(str(self.__contr.greedy(self.__p.getRoot(),self.__n)))

    def run(self):
        runM = True
        self.printMainMenu()
        while runM:
            try:
                command = int(input(">>"))
                if command == 0:
                    runM = False
                elif command == 2:
                    self.readConfigSubMenu()
                    self.findPathBFS()
                elif command == 3:
                    self.readConfigSubMenu()
                    self.findPathBestFS()
            except:
                print('invalid command')

def main():
    ui = UI()
    ui.run()


main()