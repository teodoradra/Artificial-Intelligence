# from time import time
#
# class Controller:
#     def __init__(self,problem):
#         self.__problem = problem
#
#     def greedy(selfself,root):
#         q = [root]
#
#     def DFS(self,root):
#         if root.isGoal() == True:
#             return root
#         else:
#             for i in range(len(root)):
#                 if root.isSafe(i):
#                     root.Place(i)
#                     res = self.DFS(root)
#                     if res != None:
#                         return res
#                     root.unPlace()
#
#         return None
#
#
# class Problem:
#     def __init__(self,initial,final):
#         self.__initialConfig = initial
#         self.__finalConfig = final
#         self.__initialState = State()
#         self.__initialState.setValues(self.__finalConfig)
#
#     def expand(self,currentState):
#         myList = []
#
#         return myList
#
#     def getFinal(self):
#         return self.__finalConfig
#
#     def getRoot(self):
#         return self.__initialConfig
#
#     def heuristic(self,state,finalC):
#         l = finalC.getSize()
#         count = 2*l
#
#         return l
#
#
#
#
#
# class Configuration:
#     def __init__(self,positions):
#         self._size = len(positions)
#         self._values = positions[:]
#         self.__cnt = 0
#
#     def getValues(self):
#         return self._values[:]
#
#     def getSize(self):
#         return self._size
#
#     def NextConfiguration(self,j):
#         if j >= 0 and j < self._size:
#             self._values[j] = j
#             self.__cnt += 1
#
#     def isGoal(self):
#         if self._size == self.__cnt:
#             return True
#         else:
#             return False
#
#     def unPlace(self):
#         if self.__cnt > 0:
#             self.__cnt -= 1
#
#     def isSafe(self,j):
#         for i in range(self.__cnt):
#             if self._values[i] == j or abs(j-self._values[i] == j-i):
#                 return False
#             return True
#
#     def __eq__(self, other):
#         if not isinstance(other, Configuration):
#             return False
#         if self._size != other.getSize():
#             return False
#         for i in range(self._size):
#             if self._values[i] != other.getValues()[i]:
#                 return False
#         return True
#
#     def __str__(self):
#         return str(self._values)
#
#
#
# class State:
#     def __init__(self):
#         self._values = []
#
#     def setValues(self, values):
#         self.__values = values[:]
#
#     def getValues(self):
#         return self.__values[:]
#
#     def __str__(self):
#         s = ''
#         for x in self._values:
#             s += str(x) + "\n"
#         return s
#
#     def __add__(self, something):
#         aux = State()
#         if isinstance(something, State):
#             aux.setValues(self.__values + something.getValues())
#         elif isinstance(something, Configuration):
#             aux.setValues(self.__values + [something])
#         else:
#             aux.setValues(self.__values)
#         return aux
#
#
#
#
#
#
# class UI:
#
#     def __init__(self):
#         self.__iniC = Configuration([0])
#         self.__finC = Configuration([0])
#         self.__p = Problem(self.__iniC, self.__finC)
#         self.__contr = Controller(self.__p)
#
#     def printMainMenu(self):
#         s = ''
#         s += "[RRR BBB] and [BBB RRR] are the default initial and final config.\n"
#         s += "0 - exit \n"
#         s += "1 - N = ?\n"
#         s += "2 - find a path with DFS \n"
#         s += "3 - find a path with BestFS\n"
#         print(s)
#
#     def readConfigSubMenu(self):
#         n = 3
#         try:
#             print("Input the number of red frogs (implicit n=3)")
#             n = int(input("n = "))
#         except:
#             print("invalid number, the implicit value is still 3")
#             n = 3
#         self.__iniC = Configuration([0] * n)
#         self.__finC = Configuration(['B'] * n + [0] + ['R'] * n)
#         self.__p = Problem(self.__iniC, self.__finC)
#         self.__contr = Controller(self.__p)
#
#     def findPathBFS(self):
#         startClock = time()
#         print(str(self.__contr.DFS(self.__p.getRoot())))
#         print('execution time = ', time() - startClock, " seconds")
#
#     '''   def findPathBestFS(self):
#             startClock = time()
#             print(str(self.__contr.BestFS(self.__p.getRoot())))
#             print('execution time = ', time() - startClock, " seconds")
#             '''
#
#     def run(self):
#         runM = True
#         self.printMainMenu()
#         while runM:
#             try:
#                 command = int(input(">>"))
#                 if command == 0:
#                     runM = False
#                 elif command == 1:
#                     self.readConfigSubMenu()
#                 elif command == 2:
#                     self.findPathBFS()
#                 elif command == 3:
#
#                     return
#             except:
#                 print('invalid command')
# def main():
#     ui = UI()
#     ui.run()
#
#
# main()
#
#
