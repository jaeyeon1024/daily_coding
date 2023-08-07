import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

ans = n
for i in range(m - 1):
    ans = ans % k
    ans = ans * n
print(ans % k)
