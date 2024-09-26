"""
Concealed Password
"""

password = input("Enter your password (minimum 7 characters): ")

while len(password) < 7:
    print("Password must be at least 7 characters! Try again!")
    password = input("Enter your password (minimum 7 characters): ")

length = len(password)
concealed_password = "*" * length
print(concealed_password)
