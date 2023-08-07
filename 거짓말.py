import sys
input = sys.stdin.readline

n,m = map(int,input().split())

kn = list(map(int,input().split()))

if kn[0] != 0:
    k = kn[1:]
    kn = kn[0]
board = []
for i in range(m):
    a = list(map(int,input().split()))
    board.append(a[1:])

knows = [True]+[False] * n
visited_nodes = [False] + [True] * m
check = 0
for i in k:
    knows[i] = True
while(True):
    for bd in board:
        for i in bd:
            



    if check == 0:
        break