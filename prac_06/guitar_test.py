"""Guitar Test Program
Estimated time: 20 minutes
Completion Time: 21 minutes
"""
from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar)
print(f"{guitar.name} get_age() - Expected 102. Got {guitar.get_age()}")
print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
