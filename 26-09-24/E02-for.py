from time import sleep


def all():
    for i in range(1,31):
        print(i)

def odd():
    for i in range(1,31,2):
        print(i)
        sleep(0.2)
    print("round2")
    for i in range(1,31):
        if i%2 == 1:
            print(i)
        sleep(0.2)

def sqr():
    for i in range(1,11):
        print(i**2)

sqr()