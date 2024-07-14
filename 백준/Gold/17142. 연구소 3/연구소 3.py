import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

virus_positions = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 2]

def bfs(active_viruses):
    dq = deque(active_viruses)
    distance = [[-1]*n for _ in range(n)]
    for vx, vy in active_viruses:
        distance[vx][vy] = 0
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    max_time = 0

    while dq:
        Vx, Vy = dq.popleft()

        for i in range(4):
            X = Vx + dx[i]
            Y = Vy + dy[i]

            if 0 <= X < n and 0 <= Y < n and board[X][Y] != 1 and distance[X][Y] == -1:
                distance[X][Y] = distance[Vx][Vy] + 1
                dq.append((X, Y))
                if board[X][Y] == 0:
                    max_time = max(max_time, distance[X][Y])
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and distance[i][j] == -1:
                return float('inf')
    
    return max_time

answer = float('inf')

def dfs(start, count, active_viruses):
    global answer
    if count == m:
        answer = min(answer, bfs(active_viruses))
        return
    
    for i in range(start, len(virus_positions)):
        active_viruses.append(virus_positions[i])
        dfs(i + 1, count + 1, active_viruses)
        active_viruses.pop()

dfs(0, 0, [])
print(answer if answer != float('inf') else -1)
