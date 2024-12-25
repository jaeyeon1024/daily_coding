import sys

input = sys.stdin.readline


def zzz(r,c,size,num = 0):
    if size == 1:
        return num
    size = size // 2 
    if r < size and c < size:
        pass
    elif r < size and c >= size:
        num += (size ** 2)
    elif r >= size and c < size:
        num += (size ** 2) * 2
    elif r >= size and c >= size:
        num += (size ** 2) * 3
    return zzz(r%size,c%size,size,num)
n,r,c = map(int,input().split())

print(zzz(r,c,2**n))
