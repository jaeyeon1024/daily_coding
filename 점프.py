import sys
input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(n)]


def bfs():
    cnt = 0
    discoverd = [[0, 0]]
    while discoverd:
        x, y = discoverd.pop()

        for i in range(2):
            dx = x + board[x][y] if i == 0 else x
            dy = y + board[x][y] if i == 1 else y
            if dx < n and dy < n:
                if board[dx][dy]:
                    discoverd.append([dx, dy])
                else:
                    cnt += 1

    print(cnt)
    return


bfs()
