import sys
from typing import List


def solution(ability):
    answer = 0
    per_len = len(ability)
    ability_len = len(ability[0])
    board = []
    per = []
    for i, per in enumerate(ability):
        for j ,val in enumerate(per):
            board.append((val,i,j))

    board = sorted(board, key = lambda x: (x[2],-x[0],x[1]))
    new_board = []
    
    for i in range(ability_len):
        new_board += [board[(per_len*i):ability_len+(per_len*i)][::-1]]
    print(new_board)
    
    return answer

#테니스 40 70 100
#탁구 10 30 100
#수영 30 70 100

print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
