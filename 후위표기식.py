import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input().strip())

board = list(input().strip())

dicts = defaultdict(int)

for i in range(ord('A'), ord('A') + n):
    dicts[chr(i)] = int(input().strip())

stack = deque()

for i in board:
    if i.isalpha():
        stack.append(dicts[i])
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(b+a)
        elif i == '-':
            stack.append(b-a)
        elif i == '*':
            stack.append(b*a)
        elif i == '/':
            stack.append(b/a)

print('%.2f' % stack.pop())
