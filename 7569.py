import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

board = [[list(map(int, input().split()))for __ in range(N)]for _ in range(H)]

print(board)
