"""
Get Users Email
"""


# WIll get email, split email at the @, return possible name, ask if name is correct, if not
# ask for a name from user. print email

def main():
    # email = input("Email: ")
    email = 'zmaltby@gmail.com'
    email_to_name = {}
    while email != '':
        user_information = email.split('@')
        # if user_information[0] == email_to_name.keys():
        #     print("Email already in use. Try again.")
        if '.' in user_information[0]:
            user_information[0] = user_information[0].replace('.', ' ')
        is_name(email, email_to_name, user_information)
        email = input('Email: ')
    print()
    for name, email in email_to_name.items():
        print(f"{name} ({email})")
    print("Exiting...")


def is_name(email, email_to_name, user_information):
    check_name = input(f"Is your name {user_information[0].title()}? (Y/N) ").upper()
    if check_name == 'N':
        name = input('Enter your name: ')
        email_to_name[name.title()] = email
        # print(email_to_name)
    elif check_name == 'Y':
        email_to_name[user_information[0].title()] = email
        # print(email_to_name)
    else:
        print("Invalid response...")


main()
