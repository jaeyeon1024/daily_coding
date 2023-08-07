import sys
input = sys.stdin.readline

board = list(input().rstrip())

save = 0
cnt = 0

for i, val in enumerate(board):
    if val == '(':
        cnt += 1
    else:
        cnt -= 1
        if board[i-1] == '(':
            save += cnt
        else:
            save += 1
print(save)
