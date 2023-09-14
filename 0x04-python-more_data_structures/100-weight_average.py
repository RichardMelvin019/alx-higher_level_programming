#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        denom = 0
        for tuples in my_list:
            number += (tuples[0] * tuples[1])
            denom += (tuples[1])
        return (number/denom)
    return 0
