#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:11:39 2020

@author: Teo


"""

import random
import string

def get_key(dictionary, val): 
    
    for key in dictionary.keys(): 
         if dictionary[key] == val: 
             return key 

def list_to_string(lst):
    
    string = " "
    for i in lst:
        if (i != None):
            string += i
        if (i == None):
            return None
        
    return string


def add(lst1, lst2, dictionary):
    reminder = 0
    result = []
    
    while (lst1 != [] or lst2 != []):
        
        sm = dictionary[lst1[0]] + dictionary[lst2[0]]
        
        if (sm + reminder >= 16):
            res = (sm + reminder) - 16
            reminder = sm // 16
        else:
            res =  sm + reminder
            reminder = 0
    
            
        result.append(get_key(dictionary, res))

        lst1.remove(lst1[0])
        lst2.remove(lst2[0])
            
        if ((lst1 != [] and lst2 != []) and reminder != 0):
            result.append(get_key(dictionary, reminder))
    
    return result

def diff(lst1, lst2, dictionary):
    reminder = 0
    result = []
    
    while (lst1 != [] or lst2 != []):
        
        sm = dictionary[lst1[0]] - dictionary[lst2[0]]
        
        if (sm < 0):
            res = sm + 16 - reminder
            reminder = 1
        else:
            res = sm - reminder
            reminder = 0
            
        result.append(get_key(dictionary, res))

        lst1.remove(lst1[0])
        lst2.remove(lst2[0])
    
    return result
    

def words(trials):
    
    dictionary = {}
    letters = list(string.ascii_lowercase)
    result = []
    
    lst1 = list(input("Enter first term of the operation: "))
    lst2 = list(input("Enter second term of the operation: "))
    output = input("Enter result: ")
    op = input("+/- ? ")
    
    lst1.reverse()
    lst2.reverse()
    
    
    for j in range(0, trials):
        for i in range(26):
            
            x = letters[i]
            y = random.randint(0, 15)
            dictionary[x] = y
        
        if (op == '+'):
            result = add(lst1, lst2, dictionary)
            
        elif (op == '-'):
            result = diff(lst1, lst2, dictionary)
            
        result.reverse()
    
        if (list_to_string(result) == output):
            print("Found solution!")
        else:
            print("no")
    