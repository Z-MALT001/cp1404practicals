"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# TODO When will a ValueError occur?
# If you divide by zero, enter a string, or if you enter in a float instead of an int.
# TODO When will a ZeroDivisionError occur?
# If the user enters a 0 in the denominator value.
# TODO Could you change the code to avoid the possibility of a ZeroDivisionError?
# Could ask the user to enter in a valid number then re-print, but the error will have still
# occurred. The error is caused by the user entering a zero, and theres not a way to control the
# user.