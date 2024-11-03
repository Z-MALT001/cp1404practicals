"""Guitar Test Program
Estimated time: 20 minutes
Completion Time: 21 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Run tests for Guitar class and functions."""
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2012, 1512.9)
    print(f"{guitar.name} get_age() - Expected {95}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {5}. Got {other.get_age()}\n")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


main()
