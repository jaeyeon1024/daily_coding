import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

INF = 1e8

n, m = map(int, input().split())

k = int(input().strip())

dic = {}

heap = []
visited = [False] * (n+1)
distances = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())

    if a not in dic.keys():
        dic[a] = {b: c}
    elif b in dic[a].keys():
        dic[a][b] = min(dic[a][b], c)
    else:
        dic[a][b] = c


distances[k] = 0

heapq.heappush(heap, [distances[k], k])

while heap:
    c_d, c_n = heapq.heappop(heap)

    if distances[c_n] < c_d or c_n not in dic.keys():
        continue

    for i, val in dic[c_n].items():
        if val == INF:
            continue
        distance = c_d + val
        if distance < distances[i]:
            distances[i] = distance
            heapq.heappush(heap, [distance, i])

for i in distances[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)
