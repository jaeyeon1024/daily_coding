import sys
input = sys.stdin.readline

n, m = map(int, input().split())


result = []
saves = []


def permutation(v=0):

    if len(saves) == m:
        print(*saves)
        return

    for i in range(v, n):
        saves.append(i+1)
        permutation(i)
        saves.pop()

    return result


permutation()
