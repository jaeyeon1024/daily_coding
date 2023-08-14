from typing import List
import sys
input = sys.stdin.readline


def solution(n: int, prices: List) -> None:
    sums = 0
    max_price = prices[-1]
    for pos in range(n-1, -1, -1):
        if max_price < prices[pos]:
            max_price = prices[pos]
        else:
            sums += max_price - prices[pos]
    print(sums)


cases = int(input().strip())
for _ in range(cases):
    n = int(input().strip())
    prices = list(map(int, input().strip().split()))
    solution(n, prices)
