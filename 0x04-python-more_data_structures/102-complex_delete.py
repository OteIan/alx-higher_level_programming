#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    all_values = list(a_dictionary.values())
    all_keys = list(a_dictionary.keys())
    count = 0
    for i in range(len(all_values)):
        if all_values[i] == value:
            count = i

            for j in range(len(all_keys)):
                if j == count:
                    a_dictionary.__delitem__(all_keys[j])
    if count == 0:
        return a_dictionary
    return a_dictionary
