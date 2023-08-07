import sys
input = sys.stdin.readline

board = [int(input().strip()) for _ in range(5)]

board = sorted(board)

pos = 0
while(pos < 5):
    if pos == 4:
        break
    if board[pos] == board[pos+1]:
        pos += 2
    else:
        break
print(board[pos])