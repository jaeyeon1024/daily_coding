from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [(input().strip()) for _ in range(m)]

dicts = defaultdict(int)
ans = []

for i in board:
    dicts[i] = 1

for i in board[::-1]:
    if dicts[i]:
        ans.append(i)
        dicts[i] = 0

if len(ans) < n:
    n = len(ans)

for i in range(1, n+1):
    print(ans[-i])
