"""
CP1404 Zac Maltby
Taxi Simulator
Estimated: 45 min
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    """Taxi Simulator main function"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.0

    print("Let's Drive!!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            pass
        if choice == 'd':
            pass
        else:
            print("Invalid choice...")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()


