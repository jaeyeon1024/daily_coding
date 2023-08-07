import sys
input = sys.stdin.readline

ip1 = input().strip()

board = list(map(int, ip1.replace("+", '-').split('-')))
board2 = []
for i in ip1:
    if i == '-' or i == '+':
        board2.append(i)

ans = board[0]

check = True

for i, val in enumerate(board2):
    if val == '-':
        ans -= board[i+1]
        check = False
    elif val == '+' and check:
        ans += board[i+1]
    elif val == '+' and not check:
        ans -= board[i+1]

print(ans)
