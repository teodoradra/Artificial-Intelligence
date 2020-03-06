# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:23:14 2020

@author: Teo
"""

# SUDOKU
import string
import random
from geome import main_geo
from sudoku import main_sudoku
from words import words
        
# Cripto
def generate_values():
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for e in d.keys():
        d[e] = random.randint(0,15)
    return d




input_game = input("What game? ")
input_nr_of_t = int(input("Nr of trials? "))
if (input_game == "Sudoku"):
    main_sudoku(input_nr_of_t)
elif input_game == "Cryptarithmetic":
    words(input_nr_of_t)
elif input_game == "Geometric forms":
    while (input_nr_of_t > 0):
        input_nr_of_t -= 1
        main_geo()


    
        
            

