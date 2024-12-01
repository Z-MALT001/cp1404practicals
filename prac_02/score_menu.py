"""
CP1404/CP5632 - Practical 2
Score Menu program
"""


MENU = """------------------
 Score Menu Program
(G)et a valid score (must be 0-100 inclusive
(P)rint result
(S)how stars
(Q)uit
------------------
"""

def main():
    score = get_valid_number()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")



def get_valid_number():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid input")
        score = float(input("Enter score: "))
    return score


def determine_result(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
