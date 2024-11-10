"""My Guitar Program
Estimated Completion Time: 40 minutes
"""

from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    add_new_guitars(guitars)

    display_lines()
    for guitar in sorted(guitars):
        print(guitar)

    with open(FILENAME, 'w') as out_file:
        display_lines()
        print(f"Saving guitars to {FILENAME}...")
        display_lines()
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_lines():
    print('-' * 28)


def add_new_guitars(guitars):
    """Add new guitars to the list."""
    response = input("Would you like to add new guitars? (y/n): ")
    if response.lower() == 'y':
        print("Enter an empty string for name to exit.")

        # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))  # Debugging

        name = input('Name: ')  # Error here due to it being a copy past from previous usage
        while name != '':
            year = int(input('Year: '))
            cost = float(input('Cost: $'))
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost} added.\n")
            name = input('Name: ')
        print("Exiting...\n")
    else:
        print("Moving on then...\n")


main()
