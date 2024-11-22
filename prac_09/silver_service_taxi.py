"""
CP1404 Zac Matlby
Silver Service Taxi Class
Estimated: 20 min
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with current fare distance."""
        # Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50
        return f"{super().__str__()}, ${self.price_per_km}/km plus flagfall of ${self.flagfall}"
