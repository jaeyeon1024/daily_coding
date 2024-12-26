import sys; input = sys.stdin.readline
import math
import heapq

INF = math.inf

n,e = map(int,input().split())

graph = {}

for i in range(e):
    start,end,value = map(int,input().split())
    graph[start] = graph.get(start,[]) + [[end,value]]
    graph[end] = graph.get(end,[]) + [[start,value]]

x,y = map(int,input().split())


def dijkstra(v):
    discovered = []
    visited = [0 for i in range(n+1)]
    heapq.heappush(discovered,[0,v])
    costList = [INF] * (n+1)
    costList[v] = 0

    while discovered and graph:
        cost, curV = heapq.heappop(discovered)
        visited[curV] = 1
        try:
            for V,C in graph[curV]:

                if costList[V] > cost + C:
                    if [costList[V],V] in discovered:
                        discovered.remove([costList[V],V])
                    costList[V] = cost + C
                    heapq.heappush(discovered,[costList[V],V])
        except:
            break
    return costList

startCost = dijkstra(1)  
midCost = dijkstra(x)
endCost = dijkstra(n)

if min(startCost[x] + endCost[y],startCost[y] + endCost[x]) + midCost[y] == INF:
    print(-1)
else:
    print(min(startCost[x] + endCost[y],startCost[y] + endCost[x]) + midCost[y])



