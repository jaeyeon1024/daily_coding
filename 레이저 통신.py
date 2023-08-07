import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(m)]

    count = [[0 for _ in range(n)] for _ in range(m)]
    c_pos = []
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'C':
                c_pos.append((i, j))

    def bfs():
        queue = [c_pos[0]]
        nonlocal count
        while queue:
            x, y = queue.pop(0)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx = x + dx
                ny = y + dy
                while 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '*':
                    if count[nx][ny] == 0:
                        count[nx][ny] = count[x][y] + 1
                        queue.append((nx, ny))
                    nx += dx
                    ny += dy
        return count[c_pos[1][0]][c_pos[1][1]] - 1
    print(bfs())
    return


main()
