# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 14:20:29 2020

@author: kshit
"""

def sum_name_scores(list_of_names):
    name_score = sum((i + 1) * (ord(char) - ord('A') + 1) for (i, name) in enumerate(sorted(list_of_names)) for char in name[1:-1].upper())
    return name_score

if __name__ == '__main__':
    text_file = open("p022_names.txt", "r")
    list_of_names = text_file.read().split(',')
    print(sum_name_scores(list_of_names))
            
            
