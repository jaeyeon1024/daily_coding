import sys

input = sys.stdin.readline


def main():
    n = int(input().strip())

    # 0 U: 윗 면,1 D: 아랫 면,2 F: 앞 면,3 B: 뒷 면,4 L: 왼쪽 면,5 R: 오른쪽
    # 윗면 : 흰, 아래:  노란, 앞 : 빨강, 뒷 : 오랜지, 왼 : 초록, 오른 : 파랑

    # option 0: 위 1: 오른쪽 2: 아래 3: 왼쪽
    colors = ['w', 'y', 'r', 'o', 'g', 'b']

    cube = [list(list(colors[i] for __ in range(3))for _ in range(3))
            for i in range(6)]

    move_u = [[2, 4, 3, 5], [0, 1, 2, 3]]
    move_d = [[2, 4, 3, 5], [2, 3, 0, 1]]

    move_f = [[0, 5, 1, 4], [2, 2, 0, 2]]
    move_b = [[0, 5, 1, 4], [0, 0, 2, 0]]

    move_l = [[2, 0, 3, 1], [3, 3, 3, 3]]
    move_r = [[2, 0, 3, 1], [1, 1, 1, 1]]

    for i in range(n):
        _ = input().strip()
        path = list(input().split())
        for command in path:
            if (command[0] == "U"):
                if (command[1] == "+"):
                    pass
                else:
                    pass


main()
