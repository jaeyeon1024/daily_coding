import sys
input = sys.stdin.readline


n = int(input().strip())

minus_list = []
plus_list = []

for _ in range(n):
    num = int(input().strip())
    if num <= 0:
        minus_list.append(num)
    else:
        plus_list.append(num)

minus_list.sort()
plus_list.sort(reverse=True)


minus_result = 0
plus_result = 0

for i in range(0, len(minus_list), 2):
    if i + 1 < len(minus_list):
        minus_result += minus_list[i] * minus_list[i + 1]
    else:
        minus_result += minus_list[i]


for i in range(0, len(plus_list), 2):
    if i + 1 < len(plus_list):
        if plus_list[i] == 1 or plus_list[i + 1] == 1:
            plus_result += plus_list[i] + plus_list[i + 1]
        else:
            plus_result += plus_list[i] * plus_list[i + 1]
    else:
        plus_result += plus_list[i]

print(max(minus_result+plus_result, sum(plus_list)+minus_result))
