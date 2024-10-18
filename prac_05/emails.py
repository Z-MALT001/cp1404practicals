"""
Get Users Email
"""

# WIll get email, split email at the @, return possible name, ask if name is correct, if not
# ask for a name from user. print email

# email = input("Email: ")
email = 'zac@gmail.com'
email_to_name = {}
while email != '':
    user_information = email.split('@')
    is_name = input(f"Is your name {user_information[0]}? (Y/N) ").upper()
    if is_name == 'N':
        name = input('Enter your name: ')
        email_to_name[name] = email
    elif is_name == 'Y':
        email = input('Email: ')
    else:
        print("Invalid response...")
    email = input('Email: ')