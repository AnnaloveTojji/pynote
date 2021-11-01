from copy import deepcopy

def findMaxSubmatrix(matrix, height, width):
    nrows = len(matrix)
    ncols = len(matrix[0])           

    cumulative_sum = deepcopy(matrix)

    for r in range(nrows):
        for c in range(ncols):
            if r == 0 and c == 0:
                cumulative_sum[r][c] = matrix[r][c]
            elif r == 0:
                cumulative_sum[r][c] = cumulative_sum[r][c-1] + matrix[r][c]
            elif c == 0:
                cumulative_sum[r][c] = cumulative_sum[r-1][c] + matrix[r][c]
            else:
                cumulative_sum[r][c] = cumulative_sum[r-1][c] + cumulative_sum[r][c-1] - cumulative_sum[r-1][c-1] + matrix[r][c]

    best = 0
    best_pos = None

    for r1 in range(nrows):
        for c1 in range(ncols):
            r2 = r1 + height - 1
            c2 = c1 + width - 1
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
                best_pos = r1,c1
                best = sub_sum