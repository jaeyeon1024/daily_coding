import sys
input = sys.stdin.readline

n,m = map(int,input().split())

boards = list(map(int,input().split()))

boards.sort()

check = True if boards[0]>= 0 or abs(boards[-1]) > abs(boards[0]) else False # check => + check => -

indexs = -1
for i in range(n):
    if boards[i] >=0:
        indexs = i
        break
minus_num = boards[:indexs] if indexs != -1 else boards
plus_num = boards[indexs:] if indexs != -1 else []  

sums = 0

if check and plus_num:
    sums +=abs(plus_num[-1])
    tmp = len(plus_num) - m
    if tmp <=0:
        tmp = 0
    
    plus_num = plus_num[:tmp]
elif minus_num:
    sums +=abs(minus_num[0])
    minus_num = minus_num[m:]



for i in range(len(plus_num),0,-m):
    sums += (plus_num[i-1]*2)



for i in range(0,len(minus_num),m):
    sums += (abs(minus_num[i])*2) 


print(sums)