import sys
input = sys.stdin.readline

n = int(input().strip())
board = []
lens = []
for _ in range(n):
    lens.append(int(input().strip()))
    board.append(list(map(int, input().strip().split())))

for i in range(n):
    while(True):
        flag = False
        for i ,val in enumerate(board[i]):
            if i == lens[i]-1:
                flag = True
                break
            if 