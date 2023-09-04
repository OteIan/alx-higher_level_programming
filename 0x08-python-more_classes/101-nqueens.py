#!/usr/bin/python3
from sys import argv


def main():
    if __name__ == "__main__":

        if len(argv) != 2:
            print("Usage: nqueens N")
            exit(1)
        
        num = argv[1]
        
        if not isinstance(num, int):
            print("N must be a number")
            exit(1)
        elif num < 4:
            print("N must be at least 4")
            exit(1)