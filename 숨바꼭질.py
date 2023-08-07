import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())


def bfs():
    visited = [0] * (200001)

    discovered = deque()
    discovered.append(n)
    while (discovered):
        pos = discovered.popleft()

        for i in (pos-1, pos+1, pos*2):
            if i < 0 or i > 200000:
                continue
            if visited[i] == 0 or visited[i] > visited[pos] + 1:
                visited[i] = visited[pos] + 1
                discovered.append(i)
    return visited[m]


print(bfs() if n != m else 0)
