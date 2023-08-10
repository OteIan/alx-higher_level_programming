#!/usr/bin/python3
def islower(c):
    if c == '' or c == 7:
        return False
    for i in range(ord('a'), ord('{')):
        if chr(i) == c:
            return True
    return False
