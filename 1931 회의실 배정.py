import sys
input = sys.stdin.readline

n = int(input().strip())

times = [list(map(int, input().split())) for _ in range(n)]

times.sort(key=lambda x: (x[1], x[0]))

cur = 0
ans = 0

for i in times:
    if i[0] >= cur:
        cur = i[1]
        ans += 1

print(ans)
