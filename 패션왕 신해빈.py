import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
for i in range(n):
    dicts = defaultdict(int)
    ans = 1
    m = int(input())
    if m == 0:
        print(0)
        continue
    for _ in range(m):
        _,types = input().split()
        dicts[types] += 1
    for j in dicts.values():
        ans *= (j+1)
    print(ans-1)
