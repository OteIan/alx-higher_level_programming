#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list
    for num in range(len(my_list)):
        if num == idx:
            my_list.remove(my_list[num])
    return my_list
