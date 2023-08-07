import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(map(int, input().split()))

lists = sorted(board)


result = []
saves = []


def permutation(v=0):

    if len(saves) == m:
        print(*saves)
        return

    for i in range(v, len(lists)):
        saves.append(lists[i])
        permutation(i)
        saves.pop()

    return result


permutation()
