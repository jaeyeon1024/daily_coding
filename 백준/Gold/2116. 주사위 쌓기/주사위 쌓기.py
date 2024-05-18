import sys

input = sys.stdin.readline


n = int(input().strip())

dices = [list(map(int, input().split())) for _ in range(n)]

jump_idx_dic = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

answer = 0
# top bottom은 idx or value => value
for i in range(6):
    bottom = dices[0][i]
    top = dices[0][jump_idx_dic[i]]
    sums = 0
    sums += max(
        dices[0],
        key=lambda x: (
            0 if bottom == x or top == x else x
        ),
    )

    for dice in dices[1:]:
        idx = dice.index(top)
        bottom = dice[idx]
        top = dice[jump_idx_dic[idx]]
        sums += max(
            dice,
            key=lambda x: (
                0 if bottom == x or top == x else x
            ),
        )
    answer = max(answer, sums)

print(answer)
"""

[1,0,0,0,0,1]   
[0,1,0,1,0,0]
[0,0,1,0,1,0]


시작

아래 선정 => 위 선정

제외한 가장 큰 숫자

다음층 가기
"""
