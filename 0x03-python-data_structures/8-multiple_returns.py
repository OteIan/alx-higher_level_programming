#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) is 0 or sentence is None:
        return 0, None
    return len(sentence), sentence[0]
