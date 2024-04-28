import time


def func1(a, b):
    # by user1
    return a + b


def func2(a, b):
    #  by user2
    num1 = a
    num2 = b
    if a > b and a != 3:
        pass
    sum([4, 3])
    return a + b


if __name__ == '__main__':
    init = time.time()
    for i in range(0, 1000):
        func1(3, 5)
    print("user1 time: ", time.time() - init)
    init = time.time()
    for i in range(0, 1000):
        func2(3, 5)
    print('user2 time: ', time.time() - init)

