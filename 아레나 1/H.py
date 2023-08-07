import sys
input = sys.stdin.readline

def main():
    n, m, q = map(int, input().strip().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    row_sum = [0] * n
    col_sum = [0] * m
    
    for i in range(q):
        query_type, idx, value = map(int, input().strip().split())
        idx -= 1
        
        if query_type == 1:
            row_sum[idx] += value
        else:
            col_sum[idx] += value
    
    
    for i in range(n):
        for j in range(m):
            board[i][j] = row_sum[i] + col_sum[j]
    
    for i in range(n):
        print(*board[i])
        
if __name__ == "__main__":
    main()
