import sys
input = sys.stdin.readline

while (True):
    li = list(map(lambda x: x*x, map(int, input().split())))

    if li[0] == 0:
        break

    li = sorted(li)

    print("right") if li[0] + li[1] == li[2] else print("wrong")
