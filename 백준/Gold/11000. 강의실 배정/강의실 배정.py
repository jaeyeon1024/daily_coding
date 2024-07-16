import sys
from collections import deque
import heapq

input = sys.stdin.readline


n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]

board = sorted(board, key=lambda x: (x[0], x[1]))

classes = []

min_index = 0
for start, end in board:

    if not classes:
        pass

    elif classes[0] <= start:

        heapq.heappop(classes)

    heapq.heappush(classes, end)

    # print("start, end", start, end)
    # print(classes)

print(len(classes))
