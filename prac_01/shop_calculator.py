"""
Shop Calculator
"""

MENU = """ \n Welcome to Shop Calculator!
C - To enter in your cart details
Q - Quit"""
print(MENU) # May have borrowed this piece of code, Sorry
choice = input(">>> ").upper()
total_price = 0
while choice != "Q":
    number_of_items = int(input("Enter the number of items: "))
    if number_of_items <= 0:
        print("Invalid number of items!\n")
        number_of_items = int(input("Enter the number of items: "))
    else:
        for i in range(1, number_of_items + 1):
            item_price = float(input(f"Price of item no.{i}: $"))
            total_price = total_price + item_price
        print(f"Total price for {number_of_items} is ${total_price:.2f}\n")
    print(MENU)
    choice = input(">>> ").upper()
print("\nThank you for shopping with us!")
