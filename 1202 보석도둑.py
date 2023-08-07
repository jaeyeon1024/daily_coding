import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

n, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

weight = [int(input().strip()) for _ in range(k)]


for i, val in enumerate(board):
    board[i] = (-val[1], val[0])

heapify(board)

weight = sorted(weight)

check_board = [False] * (n+1)
sums = 0
start = 0

# print(board)
# print(weight)

save_board = []

for i in weight:
    cur1 = heappop(board)
    while (save_board or board):
        if cur1[1] <= i:
            sums += -cur1[0]
            break
        else:
            heappush(save_board, cur1)
            if board:
                cur1 = heappop(board)
            else:
                break

    board = board + save_board
print(sums)


'''
4 4
1 100
14 200
13 300
10 500
10
10
13
14


'''
