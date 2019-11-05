import random

def dice():
    number = random.randint(1, 6)
    print(number)
    return number

assert 1 <= dice() <= 6