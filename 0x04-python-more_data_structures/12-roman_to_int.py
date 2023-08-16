#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    num = 0
    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    for ch in range(len(roman_string) - 1):
        if roman[roman_string[ch]] < roman[roman_string[ch + 1]]:
            num -= roman[roman_string[ch]]
        else:
            num += roman[roman_string[ch]]
    num += roman[roman_string[-1]] # Adds the last character
    return num
