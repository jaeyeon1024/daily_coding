import sys
input = sys.stdin.readline

n = int(input())
hights = [int(input().rstrip()) for _ in range(n)]

counts = list(map(int,input().split()))

hights = sorted(hights)

answer = []

for i in range(n-1,-1,-1):
    answer.append(hights[counts[i]])
    del hights[counts[i]]

for i in answer[::-1]:
    print(i)