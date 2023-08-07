import sys
input = sys.stdin.readline

n, m = map(int, input().split())


result = []


def Combination(lists, n, v=0, lens=0, saves=[]):

    if lens == n:
        result.append(saves)
        return

    for i in range(v, len(lists)):
        Combination(lists, n, i+1, lens+1, [*saves, lists[i]])

    return result


board = list(range(1, n+1))
n = m


ans = Combination(board, n)
for i in ans:
    print(*i)
