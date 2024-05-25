import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())

board = [[0 for _ in range(c+1)]]

for _ in range(r):
    board.append([0] + list(map(int, input().split())))

for row in range(1, r+1):
    for col in range(1, c+1):
        board[row][col] += board[row-1][col] + \
            board[row][col-1] - board[row-1][col-1]


for _ in range(q):
    a, b, c, d = map(int, input().split())
    tmp = board[c][d] - board[c][b-1] - board[a-1][d] + board[a-1][b-1]
    size = (c - a + 1) * (d - b+1)
    print(tmp // size)
