import sys

input = sys.stdin.readline

n = int(input().strip())
board = list(map(int,input().split()))

left = 0
right = 0
answer = 0
flag = [0] * 10
count = [0] * 10

flag[board[0]] = 1
count[board[0]] = 1

while True:
    # print(f"left {left} right {right}")
    # print(f"flag {flag} count{count}")
    if left > right:
        break
    if sum(flag) > 2:
        count[board[left]] -= 1
        if count[board[left]] == 0:
            flag[board[left]] = 0
        
        left += 1

    else:
        right +=1
        if right >= n:
            break
        count[board[right]] += 1
        flag[board[right]] = 1
    
    if sum(flag) <= 2:
        answer = max(sum(count),answer)
if n == 1:
    answer = 1

print(answer)

    
