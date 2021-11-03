# publy2- matrix of office seating, find the maximum submatrix

def solution(office, k):

    nrows = len(office)
    ncols = len(office[0])
    cumulative_sum = [[0 for x in range(nrows)] for y in range(ncols)] 
    
    for r in range(nrows):
        for c in range(ncols):
            if r == 0 and c == 0:
                cumulative_sum[r][c] = office[r][c]
            elif r == 0:
                cumulative_sum[r][c] = cumulative_sum[r][c-1] + office[r][c]
            elif c == 0:
                cumulative_sum[r][c] = cumulative_sum[r-1][c] + office[r][c]
            else:
                cumulative_sum[r][c] = cumulative_sum[r-1][c] + cumulative_sum[r][c-1] - cumulative_sum[r-1][c-1] + office[r][c]
    
    best = 0
    for r1 in range(nrows):
        for c1 in range(ncols):
            r2 = r1 + k - 1
            c2 = c1 + k - 1
            if r2 >= nrows or c2 >= ncols:
                continue
            if r1 == 0 and c1 == 0:
                sub_sum = cumulative_sum[r2][c2]
            elif r1 == 0:
                sub_sum = cumulative_sum[r2][c2] - cumulative_sum[r2][c1-1]
            elif c1 == 0:
                sub_sum = cumulative_sum[r2][c2] - cumulative_sum[r1-1][c2]
            else:
                sub_sum = cumulative_sum[r2][c2] - cumulative_sum[r1-1][c2] - cumulative_sum[r2][c1-1] + cumulative_sum[r1-1][c1-1]
            if best < sub_sum:
                best = sub_sum

    return best