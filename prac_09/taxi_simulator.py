"""
CP1404 Zac Maltby
Taxi Simulator
Estimated: 45 min
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose, d)rive"""


def main():
    """Taxi Simulator main function"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.0

    print("Let's Drive!!")
    # print(f"Bill to date: ${bill:}")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == 'd':
            bill = drive_taxi(taxis, current_taxi, bill)
        # else:
        #     print("Invalid choice...")
        print(f"Bill to date: ${bill:}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: {bill:.2f}")
    print("Taxis are now:")
    for i, taxis in enumerate(taxis):
        print(f"{i}: {taxis}")


def drive_taxi(taxis, current_taxi, bill):
    """Drive the chosen taxi"""
    if not current_taxi:
        print("You need to choose a taxi before you can drive")
    else:
        distance = int(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        bill += current_taxi.get_fare()
    return bill


def choose_taxi(taxis, current_taxi):
    """Choose a taxi"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    except ValueError:
        print("Not a valid number")
    except IndexError:
        print("Invalid option")
    return current_taxi


if __name__ == "__main__":
    main()
