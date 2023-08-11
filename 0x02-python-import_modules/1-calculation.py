#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add as plus
    from calculator_1 import sub as minus
    from calculator_1 import mul as prod
    from calculator_1 import div as div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, plus(a, b)))
    print("{} - {} = {}".format(a, b, minus(a, b)))
    print("{} * {} = {}".format(a, b, prod(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
