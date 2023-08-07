import sys
input = sys.stdin.readline

n = int(input().strip())
cases = [int(input().strip()) for _ in range(n)]
max_num = max(cases)
dp_list = [0,1,2,4] + [0] * (max_num - 3)

for i in range(4,max_num+1):
    dp_list[i] = dp_list[i-1] + dp_list[i-2] + dp_list[i-3]

for i in cases:
    print(dp_list[i])