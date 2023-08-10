#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('{')):
        if chr(i) == c:
            return True
    return False
