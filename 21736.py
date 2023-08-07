import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())

    board = [list(input().strip()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'I':
                pos = (i, j)
                break

    def bfs():
        nonlocal board
        cnt = 0
        discorverd = [pos]
        visited = [[False for _ in range(m)] for _ in range(n)]
        while discorverd:
            x, y = discorverd.pop(0)
            visited[x][y] = True
            if board[x][y] == 'P':
                cnt += 1
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx = x+dx
                ny = y+dy
                if not (0 <= nx < n) or not (0 <= ny < m) or board[nx][ny] == 'X':
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                discorverd.append((nx, ny))

        return cnt
    ans = bfs()
    print(ans if ans else 'TT')
    return


main()
