from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    name_value = defaultdict(int)

    for n,y in zip(name,yearning):
        name_value[n] = y
    
    for cases in photo:
        sums = 0
        for case in cases:
            sums += name_value[case]
        answer.append(sums)

    return answer
