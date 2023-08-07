import sys
input = sys.stdin.readline




n , k = map(int, input().split())

bags = [list(map(int,input().split())) for _ in range(n)]

values = [0] * k

bags = sorted(bags, key = lambda x : (x[0],x[1]))
print(bags)
start = 0
end = 1
sums = 0
while (start != end or end <= n):
    break
