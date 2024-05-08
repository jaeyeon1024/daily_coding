def solution(s):
    answer = 0

    ReversedList = []
    ForwardList = []
    BigRangeStr = 0

    StrList = [["{", "[", "("], ["}", "]", ")"]]

    StrDict = \
        {
            "{": "}",
            "[": "]",
            "(": ")"
        }

    start = 0
    end = len(s) - 1

    while (True):
        if start > end:
            break
        if s[start] in StrList[0]:
            ForwardList.append(s[start])
            start += 1
            continue

        if ForwardList:
            if StrDict[ForwardList.pop()] != s[start]:
                return 0
            elif not ForwardList:
                answer += 1
            start += 1
            continue

        if s[end] in StrList[1]:
            ReversedList.append(s[end])
            end -= 1
            continue

        if ReversedList:
            if StrDict[s[end]] != ReversedList.pop():
                return 0

            end -= 1
            continue
        if s[end] in StrList[0] and StrDict[s[end]] == s[start]:
            answer = 1
            start += 1
            end -= 1
            continue
        
        return 0

    if ForwardList or ReversedList:
        return 0
    return answer
