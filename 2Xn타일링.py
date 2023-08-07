import sys
input = sys.stdin.readline

n = int(input().strip())
dp_list = [0,1,2] + [0] * (n - 2)

for i in range(3,n+1):
    dp_list[i] = dp_list[i-1] + dp_list[i-2] 


print(dp_list[n] % 10007)