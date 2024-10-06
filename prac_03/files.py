"""
File reading practise
"""

# Question 1
name = input("What's your name? ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", 'r')
name_from_file = in_file.readline().strip()
print(f"Hi {name_from_file}!")
out_file.close()

# Question 3
FILENAME = "numbers.txt"

with open(FILENAME, "r") as in_file:
    result = 0

    # Approach 1
    count = 0
    for line in in_file:
        result += int(line)
        count += 1
        if count == 2:
            break
    print(result)

    # Approach 2
    numbers = in_file.readlines(3)
    result += int(numbers[0])
    result += int(numbers[1])
    print(result)

# Question 4
with open(FILENAME, "r") as in_file:
    result = 0
    for line in in_file:
        result += int(line)
    print(result)
