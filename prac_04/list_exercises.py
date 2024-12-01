"""
List Exercises
"""

numbers_str = input("Enter 5 numbers seperated by a comma: ")
# numbers_str = "1,2,3,4,5"
numbers_str = numbers_str.split(',')
# print(repr(numbers_str))
numbers = []
for number in numbers_str:
    numbers.append(int(number))
    print(f"Number: {number}")
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")



usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter yopur username: ")
if username in usernames:
    print("Access Granted!")
else:
    print("Access Denied!")
