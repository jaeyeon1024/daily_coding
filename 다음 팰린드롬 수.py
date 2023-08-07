import sys

input = sys.stdin.readline

n = int(input().strip())

board = []
even_check = len(str(n)) % 2 == 0

middle_pos = (len(str(n)) + 1) // 2 - 1
middle_str = str(n)[middle_pos]
front_str = str(n)[:middle_pos]


if even_check:
    board.append(int(front_str + middle_str + middle_str + front_str[::-1]))
else:
    board.append(int(front_str + middle_str + front_str[::-1]))


if int(middle_str) == 9:
    if front_str != "":
        front_str = str(int(front_str)+1)  
    else:
        front_str = "1"
    strs = ""
    strs += front_str
    board.append(int((strs+strs[::-1])))
    board.append(int(strs+"0"+strs[::-1]))
    board.append(int(strs+"00"+strs[::-1]))


middle_str = str(int(middle_str)+1)

if even_check:
    board.append(int(front_str + middle_str + middle_str + front_str[::-1]))
else:
    board.append(int(front_str + middle_str + front_str[::-1]))


for i in sorted(board):
    if i > n:
        print(i)
        break