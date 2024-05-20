import sys
input = sys.stdin.readline

n = int(input().strip())

dp_board = [[[0, 0] for __ in range(3)] for _ in range(2)]

for i in range(n):

    b_i = 1 if i % 2 == 0 else 0

    a, b, c = map(int, input().split())

    if i == 0:
        dp_board[i][0] = [a, a]
        dp_board[i][1] = [b, b]
        dp_board[i][2] = [c, c]

        continue

    dp_board[i % 2][0] = [max(dp_board[b_i][0][0], dp_board[b_i][1][0])+a,
                          min(dp_board[b_i][0][1], dp_board[b_i][1][1])+a]

    dp_board[i % 2][1] = [max(dp_board[b_i][0][0], dp_board[b_i][1][0], dp_board[b_i][2][0])+b,
                          min(dp_board[b_i][0][1], dp_board[b_i][1][1], dp_board[b_i][2][1])+b]

    dp_board[i % 2][2] = [max(dp_board[b_i][1][0], dp_board[b_i][2][0])+c,
                          min(dp_board[b_i][1][1], dp_board[b_i][2][1])+c]

mins = 1e8
maxs = -1

for i in dp_board[~b_i]:
    mins = min(min(i), mins)
    maxs = max(max(i), maxs)

print(maxs, mins)
