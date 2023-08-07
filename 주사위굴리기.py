import sys
input = sys.stdin.readline

'''
        back
left    down   right
        front
        up
동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로
'''


dices = [["back",0],["left",0],["down",0],["right",0],["front",0],["up",0]]

n,m,x,y,k = map(int,input().split())
board = [ list(map(int,input().split())) for _ in range(n)]

cases = list(map(int,input().split()))
for i in cases:
    if i == 1:
        if y+1 >= m:
            continue
        y += 1
    elif i == 2:
        if y-1 < 0:
            continue
        y -= 1
    elif i == 3:
        if x-1 < 0:
            continue
        x -= 1
    elif i == 4:
        if x+1>= n:
            continue
        x += 1
    for dc in range(6):
        if i == 1:
            if dices[dc][0] == "left":
                dices[dc][0] = "up"
            elif dices[dc][0] == "up":
                dices[dc][0] = "right"
            elif dices[dc][0] =="right":
                dices[dc][0] = "down"
            elif dices[dc][0] == "down":
                dices[dc][0] = "left"
        elif i == 2:
            if dices[dc][0] == "left":
                dices[dc][0] = "down"
            elif dices[dc][0] == "up":
                dices[dc][0] = "left"
            elif dices[dc][0] =="right":
                dices[dc][0] = "up"
            elif dices[dc][0] == "down":
                dices[dc][0] = "right"
        elif i == 3:
            if dices[dc][0] == "front":
                dices[dc][0] = "up"
            elif dices[dc][0] == "up":
                dices[dc][0] = "back"
            elif dices[dc][0] =="back":
                dices[dc][0] = "down"
            elif dices[dc][0] == "down":
                dices[dc][0] = "front"
        elif i == 4:
            if dices[dc][0] == "front":
                dices[dc][0] = "down"
            elif dices[dc][0] == "up":
                dices[dc][0] = "front"
            elif dices[dc][0] =="back":
                dices[dc][0] = "up"
            elif dices[dc][0] == "down":
                dices[dc][0] = "back"
    down_num =0 
    down_pos = 0
    up_num = 0
    for dc in range(6):
        if dices[dc][0] == "down":
            down_num = dices[dc][1]
            down_pos = dc
        elif dices[dc][0] == "up":
            up_num = dices[dc][1]
    
    if board[x][y] == 0:
        board[x][y] = down_num
    else:
        dices[down_pos][1] = board[x][y]
        board[x][y] = 0

    print(up_num)
