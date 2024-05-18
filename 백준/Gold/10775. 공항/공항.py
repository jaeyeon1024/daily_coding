import sys
input = sys.stdin.readline


gates = int(input().strip())
n = int(input().strip())

planes = [int(input().strip()) for _ in range(n)]

check = [True]+[False] * (gates)
remember_path = list(range(0, gates+1))
answer = 0
flag = False
for plane in planes:
    if check[plane] == False:
        answer += 1
        check[plane] = True
        remember_path[plane] = remember_path[plane-1]
        continue
    else:
        tmp = remember_path[plane]
        while check[tmp]:
            tmp = remember_path[tmp]
            if tmp == 0:
                flag = True
                break
        if flag:
            break
        remember_path[tmp] = tmp - 1
        check[tmp] = True
        remember_path[plane] = tmp - 1
        answer += 1


print(answer)
