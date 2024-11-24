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
            bill = drive_taxi(bill, current_taxi, taxis)
        else:
            print("Invalid choice...")
            print(f"Bill to date: ${bill:.2f}")
            print(MENU)
            choice = input(">>> ").lower()
        print(f"Total trip cost: {bill:.2f}")
        print("Taxis are now:")
        for i, taxis in enumerate(taxis):
            print(f"{i}: {taxis}")


def drive_taxi(taxis, current_taxi, bill):
    """Drive the chosen taxi"""
    if not current_taxi:
        print("You need to choose a taxi before you can drive.")
    else:
        distance = int(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        bill += current_taxi.get_fare()
    return bill




if __name__ == "__main__":
    main()




