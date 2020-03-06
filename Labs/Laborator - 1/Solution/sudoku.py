# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:29:32 2020

@author: Teo
"""
from collections import Counter
import random
import numpy as np
import math
import itertools
import random



def sudoku_ok(line):
    return sum(line) == sum(set(line))


def check_sums(grid):
    bad_rows = [row for row in grid if not sudoku_ok(row)]
    grid = list(zip(*grid))
    bad_cols = [col for col in grid if not sudoku_ok(col)]
    squares = []
    for i in range(len(grid), int(math.sqrt(len(grid)))):
        for j in range(len(grid), int(math.sqrt(len(grid)))):
            square = list(itertools.chain(row[j:j + int(math.sqrt(len(grid)))] for row in grid[i:i + int(math.sqrt(len(grid)))]))
            squares.append(square)
    bad_squares = [square for square in squares if not sudoku_ok(square)]
    return not (bad_rows or bad_cols or bad_squares)


def check_duplicates(row):
    length = len(row)
    counts = Counter()
    for cell in row:
        if cell != 0: counts[cell] += 1
        if cell > length or counts[cell] > 1:
            return False
    return True
#
#
def validate_result(grid):
    for row in grid:
        if not check_duplicates(row):
            return False
    submatrix = np.split(grid,
                         int(math.sqrt(len(grid))),
                         int(math.sqrt(len(grid)))
    )
    if check_sums(submatrix):
        return False
    return True
#
#
def generate_sudoku(l):
    length = len(l)
    ln = [[random.randint(1, length) for col in range(length)] for row in range(length)]
    return ln
#
#
initial_matrix4x4 = [
     [3, 0, 0, 2],
     [0, 1, 4, 0],
     [1, 2, 0, 4],
     [0, 3, 2, 1]
]
#
initial_matrix9x9 = [
     [0, 2, 0, 6, 0, 8, 0, 0, 5],
     [5, 8, 0, 0, 0, 9, 7, 0, 0],
     [0, 0, 7, 0, 4, 0, 0, 2, 8],
     [3, 7, 0, 4, 0, 1, 5, 0, 0],
     [6, 0, 0, 0, 8, 0, 0, 0, 5],
     [0, 0, 8, 0, 0, 2, 0, 1, 3],
     [8, 0, 6, 0, 2, 0, 1, 0, 0],
     [0, 0, 9, 8, 0, 0, 0, 3, 6],
     [7, 0, 0, 3, 0, 6, 0, 9, 0]
]
#
#

def main_sudoku(nr_of_t):
    nr = nr_of_t
    random_result = []

    print("4x4")
    while nr_of_t > 0:
        random_result = generate_sudoku(initial_matrix4x4)
        nr_of_t -= 1
        print("yes" if validate_result(random_result) else "no")

    print("9x9")
    while nr > 0:
        random_result = generate_sudoku(initial_matrix9x9)
        nr -= 1
        print("yes" if validate_result(random_result) else "no")

#
#if check_sums([
#    [3, 4, 2, 1],
#    [2, 1, 4, 3],
#    [4, 3, 1, 2],
#    [1, 2, 3, 4]
#]): print("yes")


