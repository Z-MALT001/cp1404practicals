"""
CP1404 Zac Matlby
Silver Service Taxi Test
Estimated: 20 min
"""

from silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Fancy Car", 100, 2)
fancy_taxi.start_fare()
fancy_taxi.drive(18)
print(fancy_taxi)
print(fancy_taxi.get_fare())
