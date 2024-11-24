"""
CP1404 Zac Matlby
Silver Service Taxi Class
Estimated: 20 min
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver Service Taxi Class"""

    def __init__(self, name, fuel, fanciness):
        """Initialise Silver Service Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        self.flagfall = 4.50

    def __str__(self):
        """Return a string like a Taxi but with current fare distance."""
        # Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def drive(self, distance):
        """Drive the Taxi by distance."""
        distance_driven = super().drive(distance)
        return distance_driven

    def get_fare(self):
        """Return the fare of the Taxi."""
        return super().get_fare() + self.flagfall
