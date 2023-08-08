from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    board = [[0 for _ in range(n+1)] for _ in range(n+1)]

    def bfs(V):  # 4
        nonlocal visited
        q = deque([V])
        while (q):
            pos = q.popleft()
            for i in graph[pos]:  # 3
                if visited[V][i] or V == i:
                    continue
                visited[V][i] = 1
                visited[i][V] = 1
                board[V][i] = board[V][pos] + 1
                board[i][V] = board[V][pos] + 1
                q.append(i)

    for i in graph.keys():
        visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
        bfs(i)

    ans = list(map(sum, board[1:]))
    print(ans.index(min(ans))+1)


main()
