#publy3 -3
# unattacking rooks

for (int i = 0; i < boardSize; i++){
    board[col][i] = 1;
    if (canPlace(col, i, board)) {
        nsolutions += findNumSolutions(board, col + 1, rooksLeft - 1);
        board[col][i] = 0;
    }
 }

 def solution(n, k):
    answer = -1
    res=n

    row = [0 for i in range(n)]
    col = [0 for i in range(n)]
    
    ri = 0
    ci = 0
	
    while (res > 0):
        while (row[ri] == 1):
            ri += 1
        while (col[ci] == 1):
            ci += 1
        answer+=1
        ri += 1
        ci += 1
        res -= 1
    
    
    
    return answer