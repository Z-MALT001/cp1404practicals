"""
Quick Picks
"""

from random import randint

AMOUNT_OF_NUMBERS = 6
MAX_NUMBER = 45
MIN_NUMBER = 1


def main():
    """Get number of quick picks to generate from user then display to user"""
    # number_of_quick_picks = input("How many quick picks would you like to generate? ")
    number_of_quick_picks = 5
    quick_picks = generate_quick_picks(number_of_quick_picks)
    for quick_pick in quick_picks:
        # print(' '.join(sorted(quick_pick, key=lambda el: int(el))))
        quick_pick = sorted(quick_pick)
        print(f"{quick_pick[0]:2} {quick_pick[1]:2} {quick_pick[2]:2} {quick_pick[3]:2} {quick_pick[4]:2} {quick_pick[5]:2}")



def generate_quick_picks(number_of_quick_picks):
    """Generate quick picks"""
    quick_picks = []
    for i in range(int(number_of_quick_picks)):
        # quick_pick = [str(randint(1, 45)) for j in range(6)]
        quick_pick = [randint(MIN_NUMBER, MAX_NUMBER) for j in range(AMOUNT_OF_NUMBERS)]
        is_repeat(quick_pick)
        quick_picks.append(quick_pick)
    return quick_picks


def is_repeat(quick_pick):
    """Check if the numbers in each quick_pick are repeated"""
    for number in quick_pick:
        if quick_pick.count(number) > 1:
            while quick_pick.count(number) > 1:
                quick_pick.remove(number)
                # quick_pick.append(str(randint(1, 45)))
                quick_pick.append(randint(MIN_NUMBER, MAX_NUMBER))


main()
