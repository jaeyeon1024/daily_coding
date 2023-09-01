import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

ans = deque([i for i in range(1, n+1)])

print("<", end="")
while ans:
    for i in range(m-1):
        ans.append(ans.popleft())
    print(ans.popleft(), end="")
    if ans:
        print(", ", end="")
print(">", end="")
