import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

row = len(str1)
col = len(str2)

dp = [[0] * col for _ in range(row)]

max_col = [0] * (col+1)
tmp_col = [0] * (col+1)
for i in range(row):
    tmp = 0
    for j in range(col):
        dp[i][j] = dp[i][j-1]

        if str1[i] == str2[j]:
            dp[i][j] = max_col[j-1] + 1

        tmp_col[j] = max(max_col[j], dp[i][j])
    max_col = tmp_col.copy()
    # print(tmp_col)

# for i in dp:
#     print(i)

print(max([max(i) for i in dp]))
'''
2차원 dp로 풀면 될거 같아서 종이에 써봄
'''
