
#problem 2334 in baekjoon OJ
from math import sqrt 

def f_distance(x1, x2, y1, y2):
    return sqrt((pow(x2 - x1, 2)) + (pow(y2 - y1, 2)))

def check_sym(arr_inp, n):
 
    if n == 2:
        print('YES')

    elif n % 2 == 0: 
        print('temp')
    else:
        print('NO')

if __name__ == '__main__':

    data_set = int(input())

    for i in range(data_set):
        dot_n = int(input())
        arr_pair = [[0 for x in range(2)] for y in range(dot_n)]

        for j in range(dot_n):
            line = input()
            a, b = line.split()
            a, b = int(a), int(b)
            arr_pair[j][0] = a
            arr_pair[j][1] = b

        check_sym(arr_pair, dot_n)

            
    

