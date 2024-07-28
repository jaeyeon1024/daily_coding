import sys
from collections import deque
input = sys.stdin.readline


w, h = map(int, input().split())


board = [list(map(lambda x: bin(int(x))[2:] if len(bin(int(x))[2:]) == 4 else '0' *
              (4-len(bin(int(x))[2:]))+bin(int(x))[2:], input().split()))for _ in range(h)]

visited = [[False]*w for _ in range(h)]


def bfs(x, y, index):

    discovered = deque()
    discovered.append((x, y))
    visited[x][y] = True
    cnt = 0

    while discovered:
        x, y = discovered.popleft()

        tmp[x][y] = index
        for i in range(4):
            if i == 0 and board[x][y][0] == '0':
                nx = x + 1
                ny = y
            elif i == 1 and board[x][y][1] == '0':
                nx = x
                ny = y + 1
            elif i == 2 and board[x][y][2] == '0':
                nx = x - 1
                ny = y
            elif i == 3 and board[x][y][3] == '0':
                nx = x
                ny = y - 1
            else:
                nx, ny = x, y

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = True
                discovered.append((nx, ny))
                cnt += 1

    return cnt


rooms = [1] * 2501
idx = 0

tmp = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if not visited[i][j]:
            rooms[idx] = bfs(i, j, idx) + 1
            idx += 1


adjacent_area = [0 for _ in range(idx)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(h):
    for j in range(w):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < h and 0 <= ny < w and tmp[i][j] != tmp[nx][ny]:
                adjacent_area[tmp[i][j]] = max(
                    rooms[tmp[i][j]] + rooms[tmp[nx][ny]], adjacent_area[tmp[i][j]])

print(idx)
print(max(rooms))
print(max(adjacent_area[:idx]))

'''

남 동 북 서

'''
