import sys
input = sys.stdin.readline

def main():
    n = int(input().strip())
    board = [input().strip() for _ in range(n)]
    m = int(input().strip())
    words = [input().strip() for _ in range(m)]

    if n == 1:
        print(words[0])
        return
    pos = 0
    for i, val in  enumerate(board):
        if val == "?":
            pos = i
            break

    for word in words:
        flag = 0
        if word in board:
            continue
        if pos+1 >= n or word[-1] == board[pos+1][0]:
            flag += 1
        if pos-1 < 0 or word[0] == board[pos-1][-1]:
            flag += 1
        
        if flag == 2:
            print(word)
            break
    return

if __name__ == "__main__":
    main()