#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    arguments = sys.argv[1:]

    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a, operator, b = arguments

    if operator == '+':
        print('{} + {} = {}'.format(a, b, add(int(a), int(b))))
    elif operator == '-':
        print('{} - {} = {}'.format(a, b, sub(int(a), int(b))))
    elif operator == '*':
        print('{} * {} = {}'.format(a, b, mul(int(a), int(b))))
    elif operator == '/':
        print('{} / {} = {}'.format(a, b, div(int(a), int(b))))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
