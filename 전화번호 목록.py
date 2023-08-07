import sys
from collections import defaultdict
input = sys.stdin.readline

cases = int(input().rstrip())
board = []

for _ in range(cases):
    save = defaultdict(list)
    n = int(input().rstrip())
    for _ in range(n):
        inputs = input().rstrip()
        save[len(inputs)].append(inputs)
    board.append(save)

for case in board:
    sort_key = sorted(case.keys())
    flag = True
    for i, val in enumerate(sort_key):
        for j in case[val]:
            for k in sort_key[i+1:]:
                for l in case[k]:
                    if j == l[:len(j)]:
                        flag = False
                        break
                if not flag:
                    break
            if not flag:
                break
        if not flag:
            break
    if flag:
        print('YES')
    else:
        print('NO')
