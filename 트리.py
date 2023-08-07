import sys
from typing import List
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input().strip())
tree = list(map(int, input().split()))
delete_num = int(input().strip())

tree_dict = defaultdict(list)
roots = 0
for i, val in enumerate(tree):
    if val == -1:
        roots = i
        continue
    tree_dict[val].append(i)

sums = 0


def dfs(V):
    global tree_dict
    global sums

    def dic_lens(arr: List) -> int:
        tmp = 0
        for i in arr:
            if i == delete_num:
                continue
            tmp += 1
        return tmp

    if V not in tree_dict or dic_lens(tree_dict[V]) == 0:
        sums += 1
        return sums
    if V == delete_num:
        return
    for i in tree_dict[V]:
        if i == delete_num:
            continue
        sums = dfs(i)
    return sums


if tree_dict == {}:
    print(0)
else:
    dfs(roots)
    print(sums)
