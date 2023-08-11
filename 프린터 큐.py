import sys
from collections import deque

num = int(sys.stdin.readline())


for i in range(num):
    n, m = map(int, sys.stdin.readline().split())
    d = deque(map(int, sys.stdin.readline().split()))
    d[m] = float(d[m])
    answer = 0

    while True:
        if int(d[0]) == int(max(d)):
            answer += 1
            if type(d[0]) == float:
                print(answer)
                break
            else:
                d.popleft()
        else:
            d.append(d.popleft())
