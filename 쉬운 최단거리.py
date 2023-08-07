import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]

    pos = [0, 0]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                pos[0] = i
                pos[1] = j
                break

    distance = [[0] * m for _ in range(n)]

    discovered = [pos]

    def bfs():
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while discovered:
            x, y = discovered.pop(0)
            for i in range(4):
                nx = x + dx[i][0]
                ny = y + dx[i][1]
                if (nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != 1 or distance[nx][ny] != 0):
                    continue
                distance[nx][ny] = distance[x][y] + 1
                discovered.append((nx, ny))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1 and distance[i][j] == 0:
                    print(-1, end=' ')
                    continue
                print(distance[i][j], end=' ')
            print()
    bfs()


main()
