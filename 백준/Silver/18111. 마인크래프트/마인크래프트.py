import sys
input = sys.stdin.readline

n, m , inven = map(int,input().split())
max_high = 0
land = []
sums = 0


for _ in range(n):
    saves = list(map(int,input().split()))
    if max(saves) > max_high:
        max_high = max(saves)
    sums += sum(saves)
    land.append(saves)

sums = (sums+inven) // (n*m) # 전체흙의 개수를 전체 칸 개수로 나누면 그게 만들 수 있는 최대 높이이다.

if sums < max_high:
    max_high = sums # 그 높이가 가장 높은 거 보다 높으면 그냥 가장 높은 곳 기준으로 쌓는게 이득이다.

counters = 0
up_time = 0
for high in range(max_high,-1,-1): # 가능한 가장 높은 곳에서부터 내려온다. 
    down_time = 0    
    for i in range(n):
        for j in range(m):
            a = land[i][j] - (high - 1) # 높이와 현재 쌓여있는 높이의 차이
            if a < 0: # 흙이 부족하면 더 쌓는시간을 더한다.
                down_time += -a # 음수니깐 - 붙여서 더하기
            elif a > 0: #흙이 더 많으면 흙을 부순다.
                down_time += a * 2 # 흙을 제거하는 연산이니깐 *2를 해서 더하기
            if high == max_high: # 처음 시작 할 때만 현재 높이 계산
                b = land[i][j] - (high) # 한칸 낮은 곳의 높이의 차이 
                if b < 0: #아래층도 똑같이 계산 해준다
                    up_time += -b
                elif b > 0:
                    up_time += b * 2
    if up_time <= down_time: # 아래층으로 만드는 시간보다 위층을 만드는 시간이 덜 걸리면 그게 시간 최소값이다
        print(up_time, high)
        break
    up_time = down_time