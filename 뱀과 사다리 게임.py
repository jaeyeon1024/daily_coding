import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int, input().split())

move = [list(map(int,input().split())) for _ in range(n+m)]

move_dict = defaultdict(int)

for i in range(n+m):
    move_dict[move[i][0]] = move[i][1]

board = [0] * 101


def bfs():
    q = deque([1])

    
    while q:
        x = q.popleft()
        if x == 100:
            print(board[x])
            return
        for i in range(1,7):
            dx = x + i
            if dx > 100:
                continue
            if dx in move_dict.keys():
                dx = move_dict[dx]
            if board[dx] == 0 or board[dx] > (board[x] + 1):
                board[dx] = board[x] + 1
                q.append(dx)
    return

bfs()