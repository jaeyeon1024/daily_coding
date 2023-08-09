'''

3 4

1 1 1   1 1
2 2 2   2 2
3 3 3   0 3
1 4 4   1 0
2 1 5   2 1
3 2 6   0 2
1 3 7 
2 4 8
3 1 9




n, m, i mod n, i mod m 이 주어질 때 i를 구하는 알고리즘

'''


import sys
import math
input = sys.stdin.readline

n = int(input().strip())

board = [list(map(int, input().split())) for _ in range(n)]

for case in board:
    a, b, c, d = case
    ans = 0
    if a == 1 and b == 1:
        if c == 1 and d == 1:
            print(1)
            continue
        print(-1)
        continue

    tmp1 = math.lcm(a, b)

    a_list = []
    b_list = []

    for i in range(c, tmp1+1, a):
        a_list.append(i)
    for i in range(d, tmp1+1, b):
        b_list.append(i)

    a_list.extend(b_list)
    a_list = sorted(a_list)

    for i, val in enumerate(a_list):
        if i == len(a_list)-1:
            print(-1)
            break
        if val == a_list[i+1]:
            print(val)
            break
