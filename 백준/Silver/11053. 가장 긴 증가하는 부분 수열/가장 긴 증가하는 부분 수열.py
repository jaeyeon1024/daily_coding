import sys
input = sys.stdin.readline

n = int(input().strip())

board = list(map(int, input().split()))

increase_board = [1] + [0] * (n-1)


for i, val in enumerate(board):
    if i == 0:
        continue
    smaller_idx = list(filter(lambda x: val > board[x], range(i)))

    if smaller_idx:
        max_idx = max(smaller_idx, key=lambda x: increase_board[x])
        increase_board[i] = increase_board[max_idx] + 1
    else:
        increase_board[i] = 1

print(max(increase_board))
