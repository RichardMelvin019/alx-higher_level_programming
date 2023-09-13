#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    added_list = []

    for i in my_list:
        if i % 2 == 0:
            added_list.append(True)
        else:
            added_list.append(False)
    return (added_list)
