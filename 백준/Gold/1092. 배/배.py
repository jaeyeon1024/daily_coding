import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input().strip())
crains = list(map(int, input().split()))
m = int(input().strip())
boxs = list(map(int, input().split()))

time = 0

crains.sort()
boxs.sort(reverse=True)

crains_tmp = [[0] for _ in range(n)]

max_height = 0

for box in boxs:
    for idx, crain in enumerate(crains):
        if box <= crain:

            if len(crains_tmp[idx]) > len(min(crains_tmp[idx:], key=lambda x: len(x))):
                continue
            crains_tmp[idx].append(box)

            break

if max(boxs) > max(crains):
    print(-1)
else:
    print(len(max(crains_tmp[:], key=lambda x: len(x))) - 1)

"""

dic로 했다가 같은 크레인 처리가 불가능 하여 다른 걸로 바꿈


"""
