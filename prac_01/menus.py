"""
Menu Program
"""

name = input("Hello, whats your name? ")
menu = """Simple Menu Program
H - Greetings
G - Goodbyes 
Q - Quit
"""
print(f" \nHello {name}, Welcome to a...\n")
print(menu)
choice = input(">>> ").upper()
while choice != 'Q':
    if choice == 'H':
        print(f"Hello again {name}\n")
    elif choice == 'G':
        print(f"Goodbye {name} :,(\n")
    else:
        print("Invalid message\n")
    print(menu)
    choice = input(">>> ").upper()
print(f"\nShutting Down...")
