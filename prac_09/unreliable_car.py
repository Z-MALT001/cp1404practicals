"""
CP1404 Zac Matlby
Unreliable Car Class
Estimated: 20 min
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""
    def __init__(self, name, fuel, reliability: float):
        """Initialise UnreliableCar Class, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        # Reliability Skill Check
        if randint(0, 100) > self.reliability:
            distance_driven = super().drive(0)
        else:
            distance_driven = super().drive(distance)
        return distance_driven
