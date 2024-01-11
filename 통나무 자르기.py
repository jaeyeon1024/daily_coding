import sys
input = sys.stdin.readline

L, K, C = map(int, input().split())
board = list(set(map(int, input().strip().split())))

board.sort()

left = 1
right = L

L_pos = 0
R_pos = len(board)-1

while(left + 1 != right):
    lens = L - (board[L_pos] + (L - board[R_pos]))
    cnt = C - 2 if len(board) < C else len(board)

    while(cnt):
        





