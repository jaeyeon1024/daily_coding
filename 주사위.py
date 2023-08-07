import sys
input = sys.stdin.readline

n = int(input().strip())
board = list(map(int, input().strip().split()))

board = sorted(board)

ans = 0

ans += ((n-2) * board[0]) * ((n-2)**2) * 5
ans += ((n-1) * sum(board[:2])) * 4
ans += ((n-2) * sum(board[:2])) * 4
ans += (sum(board[:3])) * 4
print(ans)
