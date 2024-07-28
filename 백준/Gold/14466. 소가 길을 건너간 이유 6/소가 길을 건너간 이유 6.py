import sys
input = sys.stdin.readline


n, k, r = map(int, input().split())

board = [['0000']*n for _ in range(n)]

for _ in range(r):
    a, b, c, d = map(int, input().split())
    if a == c:
        if b < d:
            board[a-1][b-1] = '1' + board[a-1][b-1][1:]
            board[c-1][d-1] = board[c-1][d-1][:1] + '1' + board[c-1][d-1][2:]
        else:
            board[a-1][b-1] = board[a-1][b-1][:1] + '1' + board[a-1][b-1][2:]
            board[c-1][d-1] = '1' + board[c-1][d-1][1:]
    else:
        if a < c:
            board[a-1][b-1] = board[a-1][b-1][:2] + '1' + board[a-1][b-1][3]
            board[c-1][d-1] = board[c-1][d-1][:3] + '1'
        else:
            board[a-1][b-1] = board[a-1][b-1][:3] + '1'
            board[c-1][d-1] = board[c-1][d-1][:2] + '1' + board[c-1][d-1][3]

cows = [list(map(int, input().split())) for _ in range(k)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tmp_board = [[-1]*n for _ in range(n)]


def bfs(x, y):

    discovered = []
    discovered.append((x, y))
    cnt = 0

    while discovered:
        x, y = discovered.pop()
        if tmp_board[x][y] == -1:
            tmp_board[x][y] = index

        for i in range(4):
            if i == 0 and board[x][y][0] == '0':
                nx = x
                ny = y + 1
            elif i == 1 and board[x][y][1] == '0':
                nx = x
                ny = y - 1
            elif i == 2 and board[x][y][2] == '0':
                nx = x + 1
                ny = y
            elif i == 3 and board[x][y][3] == '0':
                nx = x - 1
                ny = y
            else:
                nx, ny = x, y

            if 0 <= nx < n and 0 <= ny < n and tmp_board[nx][ny] == -1:
                if tmp_board[nx][ny] == index:
                    continue
                tmp_board[nx][ny] = index
                discovered.append((nx, ny))


for i in range(k):
    index = i
    x, y = cows[index]
    bfs(x-1, y-1)

count = [0]*k

# for i in tmp_board:
#     print(i)

for i in range(k):
    count[tmp_board[cows[i][0]-1][cows[i][1]-1]] += 1

print(k*(k-1)//2 - sum(map(lambda x: x*(x-1)//2 if x > 1 else 0, count)))


'''
동 서 남 북
'''
