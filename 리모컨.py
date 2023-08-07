import sys
input = sys.stdin.readline


def main():
    N = (input().strip())

    m = int(input().strip())
    board = [abs(int(N) - 100)]
    saves = []
    min_num = -1
    max_num = -1
    if not m == 0:
        check_list = list(map(int, input().split()))
    else:
        print(min(abs(int(N) - 100), len(N)))
        return

    for i in range(1000001):
        flag = True
        for j in str(i):
            if int(j) in check_list:
                flag = False
                break
        if not flag:
            continue
        saves.append(i)
        if i <= int(N):
            min_num = i
        if i >= int(N):
            max_num = i
            break
    if len(saves) == 0:
        print(abs(int(N) - 100))
        return
    if min_num != -1:
        board.append(abs(int(N) - min_num)+len(str(min_num)))
    if max_num != -1:
        board.append(abs(int(N) - max_num)+len(str(max_num)))

    print(min(board))


main()
