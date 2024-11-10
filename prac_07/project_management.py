"""Project management
Estimated Completion Time: 1 hour

"""
import datetime

date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
print(f"That day is/was {date.strftime('%A')}")
print(date.strftime("%d/%m/%Y"))


FILENAME = "projects.txt"
MENU = """(L)oad projects  
(S)ave projects  
(D)isplay projects  
(F)ilter projects by date
(A)dd new project  
(U)pdate project
(Q)uit"""

def main():
    print("Welcome to Pythonic Project Management")
    print(f"Loaded 5 projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
        elif choice == "S":
        elif choice == "D":
        elif choice == "F":
        elif choice == "U":
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

