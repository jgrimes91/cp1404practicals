import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Quick picks program - choose a random set of numbers"""
    user_pick = int(input("How many quick picks? "))
    while user_pick < 0:
        print("Please choose a valid number")
        user_pick = int(input("How many quick picks? "))

    for i in range(user_pick):
        quick_pick = []
        for n in range(NUMBERS_PER_LINE):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
