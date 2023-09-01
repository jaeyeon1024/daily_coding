import sys
input = sys.stdin.readline

n = int(input().strip())

board = [list(map(int, input().strip().split())) for _ in range(n)]

dp = [0 for _ in range(n)]


for i, val in enumerate(board):
    pos = board[i][0] + i - 1
    if pos >= n:
        continue
    if dp[pos] == 0 or dp[pos] < board[i][1]:
        dp[pos] = board[i][1] + dp[i]

print(board)
print(dp)
