
result = []


def permutation(lists, n, lens=0, saves=[]):

    if lens == n:
        result.append(saves)
        return

    for i in range(len(lists)):
        if lists[i] in saves:
            continue
        permutation(lists, n, lens+1, [*saves, lists[i]])

    return result


board = [1, 2, 3]
n = 2

print(permutation(board, n))
