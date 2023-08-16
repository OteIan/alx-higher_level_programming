#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    total_weight = 0
    total_score = 0
    for score, weight in my_list:
        total_weight += (score * weight)
        total_score += weight
        # I'm sorry if you don't understand this
        # It works so i'm not touching it
    if total_score == 0:
        return 0
    return total_weight / total_score
