import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().strip())
a, b = map(int, input().split())
m = int(input().strip())
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start, end):
    queue = [start]
    visited = [0]*(n+1)
    visited[start] = 1
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v]+1
    return visited[end]-1


print(bfs(a, b))
