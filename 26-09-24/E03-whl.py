from random import randint


def a():
    # do not use this will cause an infinite loop
    while True: print(randint(-100,5))

def b():
    limit = int(input("please give me an uper limit, all numbers produced will be less than \
                  your given number"))
    while True: print(randint(-limit, limit-1))