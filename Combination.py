
result = []


def Combination(lists, n, v=0, lens=0, saves=[]):

    if lens == n:
        result.append(saves)
        return

    for i in range(v, len(lists)):
        Combination(lists, n, i+1, lens+1, [*saves, lists[i]])

    return result


board = [1, 2, 3]
n = 2

print(Combination(board, n))
