
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

#  What did you see on line 1?
# I saw a random number from 5 to 20.
#  What was the smallest number you could have seen, what was the largest?
# 5 was the smallest number I could have seen, 20 was the highest.
#
#  What did you see on line 2?
# I saw a random range from 3 to 10, with 2-step intervals, so 3, 5, 7, 9.
#  What was the smallest number you could have seen, what was the largest?
# The smallest number I could've seen was 3, the largest was 9.
#  Could line 2 have produced a 4?
# No it could not have because its only capable of producing odd numbers.
#
#  What did you see on line 3?
# I saw a random integer with 16 decimal places in range from 2.5 to 5.5.
#  What was the smallest number you could have seen, what was the largest?
# The smallest number I could have see was 2.5000000000000, and largest being 5.50000000000,
# but both of these possabilities are unlikely due to the amount of decimal places.
#  Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100)) # random number from 1 to 100 inclusive