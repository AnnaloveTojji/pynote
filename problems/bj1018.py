# bj1018 체스판 다시 칠하기
board = []
n, m = map(int, input().split())

chess = []
for _ in range(n):
    row = list(map(int,input().split()))
    board.append(row)
for i in range(m-7):
    for j in range(n-7):
        if board[i][j] != chess[i][j]:
            count+=1