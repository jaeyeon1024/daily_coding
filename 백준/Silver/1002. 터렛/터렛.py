import sys

input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    x, y, r1, n, m, r2 = map(int, input().split())

    dis = ((x - n) ** (2) + (y - m) ** (2)) ** (1 / 2)

    if dis == 0 and r1 == r2:
        print(-1)
    elif r1 + dis == r2 or r2 + dis == r1 or dis - r1 == r2:
        print(1)
    elif r1 > dis and dis + r2 < r1 or r2 > dis and dis + r1 < r2:
        print(0)
    elif r1 + r2 < dis:
        print(0)

    else:
        print(2)
