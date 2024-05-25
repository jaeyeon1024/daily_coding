import sys
input = sys.stdin.readline

n = int(input().strip())

board = list(map(int, input().split()))

increase_board = [1] + [0] * (n-1)
reverse_board = [1] + [0] * (n-1)

for i, val in enumerate(board):
    if i == 0:
        continue
    smaller_idx = list(filter(lambda x: val > board[x], range(i)))

    if smaller_idx:
        max_idx = max(smaller_idx, key=lambda x: increase_board[x])
        increase_board[i] = increase_board[max_idx] + 1
    else:
        increase_board[i] = 1


for i, val in enumerate(board[::-1]):
    if i == 0:
        continue
    bigger_idx = list(filter(lambda x: val > board[n-x-1], range(i)))

    if bigger_idx:
        max_idx = max(bigger_idx, key=lambda x: reverse_board[x])
        reverse_board[i] = reverse_board[max_idx] + 1
    else:
        reverse_board[i] = 1

print(max([i+j for i, j in zip(increase_board, reverse_board[::-1])]) - 1)
