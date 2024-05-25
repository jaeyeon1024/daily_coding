def solution(n):

    board = [1, 1] + [0] * n

    for i in range(2, len(board)):
        board[i] = (board[i-1] + board[i-2]) % 1234567

    return board[n]