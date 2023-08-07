import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def find_third_num(size):
    if size == 1:
        return 


n = int(input().strip())

board = [list(map(int,input().split())) for i in range(n)]

