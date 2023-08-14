#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first 2 integers from each tuple
    # Or use 0 if not available
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Calculate the sum of the corresponding elements in each tuple
    sum_first = a[0] + b[0]
    sum_second = a[1] + b[1]

    return sum_first, sum_second
