"""
CP1404 Zac Matlby
Unreliable Car Test
Estimated: 20 min
"""

from prac_09.unreliable_car import UnreliableCar

for i in range(1, 10):
    my_car = UnreliableCar("Commodore", 100, 80)
    my_car.drive(40)
    print(f"{my_car}")
    my_car.drive(10)
    print(f"{my_car}")
