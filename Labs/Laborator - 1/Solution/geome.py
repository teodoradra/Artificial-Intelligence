# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:40:32 2020

@author: Teo
"""
import random

f1 = [(0,-1),(1,0),(1,0),(1,0),(0,1)]
f2 = [(1,0),(1,0),(1,0),(1,0)]
f3 = [(-1,0),(1,0),(1,0)]
f4 = [(1,0),(1,0),(0,-1)]
f5 = [(1,0),(0,1),(1,-1)]


def check_geo(l,f):
    c = random.randint(0,3)
    r = random.randint(0,4)
    for t in f:
        if  r>=5 or c>=4 or r<0 or c<0:
            return False,l
        if l[r][c] == 1:
            return False,l
        l[r][c] += 1
        tc, tr = t
        r = r + tr
        c = c + tc
    return True,l
        
def main_geo():
    matr = [[0 for col in range(0,4)] for row in range(0,5)]
    f = [f1,f2,f3,f4,f5]
    for form in f:
        yes , matr = check_geo(matr,form)
        if not yes:
            print("no")
            break

