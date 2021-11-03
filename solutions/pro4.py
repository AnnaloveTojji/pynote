#diagonal difference
def diagonalDifference(arr):
    # Write your code here
    d1 = sum([arr[x][x] for x in range(len(arr))])
    d2 = sum([arr[x][n - 1 - x] for x in range(len(arr))])
    return(abs(d1 - d2))


def sol(arr):
        
    x = len(arr)
    d1 = sum([arr[i][i] for i in range(x)])
    d2 = sum([arr[i][x-1-i] for i in range(x)])
    
    if d1 > d2:
        return(d1-d2)
    elif d2>d1:
        return(d2-d1)
    else:
        return(0)


  