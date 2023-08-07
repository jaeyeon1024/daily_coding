import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n-1)]
    question = [list(map(int, input().split())) for _ in range(m)]

    graph_dict = defaultdict(list)
    for i in graph:
        graph_dict[i[0]].append((i[1], i[2]))
        graph_dict[i[1]].append((i[0], i[2]))

    def bfs(i):
        nonlocal graph_dict
        nonlocal n
        node_distance = [0] * (n+1)
        discovered = [i[0]]
        visited = [False] * (n+1)
        while (True):
            pos = discovered.pop(0)
            if node_distance[i[1]] != 0:
                print(node_distance[i[1]])
                break

            visited[pos] = True
            
            for j in graph_dict[pos]:
                if visited[j[0]]:
                    continue
                node_distance[j[0]] = node_distance[pos] + j[1]
                discovered.append(j[0])

    for i in question:
        bfs(i)


main()

'''

[0,0,0,0,0]

4 2
2 1 2
4 3 2
1 4 3
1 2
3 2

'''
