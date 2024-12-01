"""
CP1404/CP5632 - Practical 2
Refactored program to determine score status
"""

from random import randint

def main():
    score = float(input("Enter score: "))
    result = calculate_score(score)

    print(result)
    print("\nNext result is a random score")
    score = randint(0, 100)
    result = calculate_score(score)
    print(f"Random score is {score}")
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
