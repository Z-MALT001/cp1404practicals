"""My Guitar Program
Estimated Completion Time: 40 minutes
"""

import csv
from collections import namedtuple
from guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

        for guitar in sorted(guitars):
            print(guitar)


main()
