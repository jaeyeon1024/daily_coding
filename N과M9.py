import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(map(int, input().split()))

lists = sorted(board)

result = []


def permutation(saves=[]):

    if len(saves) == m and saves not in result:
        result.append(saves)
        return

    for i in range(len(lists)):
        if lists[i] in saves and saves:
            continue
        permutation([*saves, lists[i]])

    return result


print(permutation())
