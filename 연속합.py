import sys
input = sys.stdin.readline

n = int(input().strip())

board = list(map(int, input().strip().split()))


dp = [0] * n

dp[0] = board[0]

for i in range(1, n):

    dp[i] = max(board[i], board[i] + dp[i-1])

print(max(dp))
