import sys
input = sys.stdin.readline

n = int(input().strip())

flower_board = []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    start = a * 100 + b
    end = c * 100 + d
    flower_board.append((start, end))

# 꽃의 시작 날짜를 기준으로 오름차순 정렬하되, 시작 날짜가 같으면 끝나는 날짜를 기준으로 내림차순 정렬
flower_board.sort(key=lambda x: (x[0], -x[1]))

cnt = 0
current_end = 301
max_end = 0
index = 0

while index < n:
    found = False
    while index < n and flower_board[index][0] <= current_end:
        if flower_board[index][1] > max_end:
            max_end = flower_board[index][1]
            found = True
        index += 1
    
    if not found:
        break

    current_end = max_end
    cnt += 1

    if current_end > 1130:
        print(cnt)
        sys.exit(0)

print(0)
