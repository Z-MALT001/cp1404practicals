"""
Concealed Password
"""


def main():
    password = get_password()

    length = len(password)
    concealed_password = "*" * length
    print_password(concealed_password)


def print_password(concealed_password):
    print(concealed_password)


def get_password():
    password = input("Enter your password (minimum 7 characters): ")
    while len(password) < 7:
        print("Password must be at least 7 characters! Try again!")
        password = input("Enter your password (minimum 7 characters): ")
    return password


main()
