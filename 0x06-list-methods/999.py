#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None

    for i in (len(my_list) - 1):
        if i == idx:
            return my_list[i]

    return None
