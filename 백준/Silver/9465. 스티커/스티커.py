import sys

input = sys.stdin.readline


cases = int(input().strip())

for _ in range(cases):
    n = int(input().strip())

    board = [list(map(int, input().split())) for _ in range(2)]

    score = [[0] * n for _ in range(2)]

    for i in range(n):

        if i == 0:
            score[0][i] = board[0][i]
            score[1][i] = board[1][i]
            continue
        if i == 1:
            score[0][i] = score[1][i-1] + board[0][i]
            score[1][i] = score[0][i-1] + board[1][i]
            continue

        score[0][i] = score[1][i-1] + board[0][i] if score[1][i-1] + \
            board[0][i] > score[1][i-2] + board[0][i] else score[1][i-2] + board[0][i]
        score[1][i] = score[0][i-1] + board[1][i] if score[0][i-1] + \
            board[1][i] > score[0][i-2] + board[1][i] else score[0][i-2] + board[1][i]

    print(max([max(i) for i in score]))
