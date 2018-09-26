import random
from math import sqrt
def random_cal_pi():
    print("input n:")
    n = int(input())
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if sqrt(x * x + y * y)<1:
            count += 1
    mypi = 4 * count / n
    print("my pi is",mypi)

if __name__ == '__main__':
    random_cal_pi()
