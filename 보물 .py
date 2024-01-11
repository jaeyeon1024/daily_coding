import sys
input = sys.stdin.readline

n = int(input().strip())

A_board = list(map(int, input().strip().split()))
B_board = list(map(int, input().strip().split()))

A_board.sort()
B_board.sort(reverse=True)

result = 0

for i in range(n):
    result += A_board[i] * B_board[i]

print(result)
