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
            read_from_file()
        elif choice == "S":
            write_to_file(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "U":
            return update_project_status(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using Pythonic Project Management")


def update_project_status(projects):
    """Update specific project completion percentage, and priority"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice_index = int(input("Project Choice: "))
    while project_choice_index > len(projects):
        print("Invalid choice")
        project_choice = int(input("Project Choice: "))
    project_choice = projects[project_choice_index]
    print(project_choice)

    completion_percentage = int(input("New Completion Percentage: "))
    while not (0 <= completion_percentage <= 100):
        print("Invalid choice")
        completion_percentage = int(input("New Completion Percentage: "))
    priority = int(input("Priority: "))
    while priority <= 0:
        print("Invalid choice")
        priority = int(input("Priority: "))
    priority = int(priority)

    project_choice.completion_percentage = completion_percentage
    project_choice.priority = priority
    projects[project_choice_index] = project_choice
    return projects


def write_to_file(projects):
    out_filename = input("Enter the name of the output file: ")
    # Name	Start Date	Priority	Cost Estimate	Completion Percentage
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage")
    with open(out_filename, "w") as out_file:
        for project in projects:
            out_file.write(f"{project.line_format()}\n")


def read_from_file():
    """Read data from file"""
    projects = []
    # Name	Start Date	Priority	Cost Estimate	Completion Percentage
    number_of_projects = 0
    try:
        with open(FILENAME, "r") as in_file:
            in_file.readline()  # get rid of header
            for line in in_file:
                parts = line.strip().split('\t')
                projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))  # add to list of projects
                number_of_projects += 1
        print(f"Loaded {number_of_projects} projects from {FILENAME}")
    except FileNotFoundError:
        print(f"File not found: {FILENAME}")
    return projects


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
