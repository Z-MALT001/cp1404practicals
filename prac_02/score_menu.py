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
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
            result = calculate_score(score)
            print(result)



def calculate_score(score):
    if score < 0 or score > 100:
        result = "Invalid score"
        return result
    elif score < 50:
        result = "Bad"
        return result
    elif score < 90:
        result = "Passable"
        return result
    else:
        result = "Excellent"
        return result


main()
