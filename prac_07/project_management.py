"""Project management
Estimated Completion Time: 1 hour

"""
import datetime
import json
from prac_07.project import Project

# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))


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
    projects = read_from_file()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using Pythonic Project Management")


def display_projects(projects):
    """Display organised projects to user"""
    print("Incomplete projects")
    incomplete_projects = [f"\t{project}" for project in projects if not project.is_complete()]
    print('\n'.join(incomplete_projects))
    print("Complete projects")
    complete_projects = [f"\t{project}" for project in projects if project.is_complete()]
    print('\n'.join(complete_projects))


if __name__ == '__main__':
    main()
