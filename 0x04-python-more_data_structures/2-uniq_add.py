#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    sum_ = 0
    for i in new_list:
        sum_ = sum_ + i
    return sum_
