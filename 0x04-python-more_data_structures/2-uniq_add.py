#!/usr/bin/python3

def uniq_add(my_list=[]):
    num = 0
    for item in set(my_list):
        num += item
    return num
