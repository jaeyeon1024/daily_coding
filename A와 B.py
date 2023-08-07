import sys
input = sys.stdin.readline

strs1 = input().strip()
target = input().strip()

while (len(target) > len(strs1)):
    if target[-1] == 'A':
        target = target[:-1]
    else:
        target = target[:-1][::-1]
print(1 if target == strs1 else 0)
