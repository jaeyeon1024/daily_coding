import sys
input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())

    board = []

    if m % 10 == 1:
        board.append(m//10)
    if m % 2 == 0:
        board.append(m//2)

    cnt = 1
    tmp = []
    while (True):
        while (board):
            i = board.pop()
            if i == n:
                print(cnt+1)
                return
            if i % 10 == 1 and i != 1:
                tmp.append(i//10)
            if i % 2 == 0:
                tmp.append(i//2)

        if not tmp:
            print(-1)
            return

        board.clear()
        board.extend(tmp)
        tmp.clear()
        cnt += 1


solution()
