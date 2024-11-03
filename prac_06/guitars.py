"""Guitars Program
Estimated Time: 20 minutes
Actual Time: 25 minutes
"""

from prac_06.guitar import Guitar

guitars = []
name = input('Name: ')
while name != '':
    year = int(input('Year: '))
    cost = float(input('Cost: $'))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost} added.\n")
    name = input('Name: ')
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print("... snip ...")
print("These are my guitars:")
max_name_length = max(len(guitar.name) for guitar in guitars)
for i, guitar in enumerate(guitars, start=1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
