import sys

input = sys.stdin.readline

n,k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

board = sorted(board)

weightMap = [[0] * (k+1) for _ in range(n+1)]

for i in range(n):
    for j in range(k+1):
        if j < board[i][0]:
            weightMap[i][j] = weightMap[i-1][j]
            continue
        
        # print(f"i : {i} j : {j} board[i][1] : {board[i][1]} weightMap[i-1][k-board[i][0]] : { weightMap[i-1][k-board[i][0]]}")

        if j == board[i][0]:
            # print("1")
            weightMap[i][j] = max(weightMap[i-1][j],board[i][1])
        else:
            # print("2")
            weightMap[i][j] = max(weightMap[i-1][j],board[i][1]+weightMap[i-1][j-board[i][0]])
        
#         print(weightMap)

# print(weightMap)
print(weightMap[-2][-1])
