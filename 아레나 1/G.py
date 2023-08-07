import sys
input = sys.stdin.readline

def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # 중복 계산 방지
                factors.append(n // i)
    return sorted(factors)[:len(factors)-1]

n = int(input().strip())
n_num = list(map(int, input().strip().split()))
m = int(input().strip())
m_num = list(map(int, input().strip().split()))

n_num = sorted(n_num)

for i in m_num:
    ans = 0
    dx = 0
    if i == 1:
        print(1, end=" ")
        continue
    factors = find_factors(i)
    for j in n_num:
        if i == j:
            ans += 1
        if j > i:
            break
        for k in factors:
            if k % j == 0:
                ans += 1
            
    print(ans, end=" ")