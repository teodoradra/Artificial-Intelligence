# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:29:36 2020

@author: Teo
"""


import matplotlib.pyplot as plt
import numpy as np

while(True):
    distr_str = input("Choose distribution (1 - Uniform, 2 - Gamma):")
    distr_mapping = {
        1: np.random.uniform,
        2: np.random.gamma,
        3: np.random.normal
    }
    distr_type = distr_mapping.get(int(distr_str))
    number = int(input("How many:"))
    if distr_str == '1':
        from_value = int(input("From:"))
        to_value = int(input("To:"))
        plt.plot(distr_type(from_value, to_value, number))
    elif distr_str == '2':
        loc = int(input("Shape:"))
        plt.plot(distr_type(loc, 1, number))
    expected = list(input("Expected:").split(' '))
    plt.plot(expected)
    plt.ylabel('some values')
    plt.show()