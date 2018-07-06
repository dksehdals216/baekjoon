
#baekjoon problem 11371
from math import atan, pi

if __name__ == '__main__':
    while True:
        inp = input()
        a, b = inp.split()
        a, b = float(a), float(b)
        if a == 0 and b == 0:
            break
        elif b == 0:
            print(0)
        elif a == 0:
            print(90)
        else:
            val = (180 * atan(b/a))/pi
            print(round(val))





