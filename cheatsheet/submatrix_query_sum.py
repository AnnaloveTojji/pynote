# Python 3 program to compute submatrix
# query sum in O(1) time

M = 6
N = 6

# Function to preprcess input mat[M][N].
# This function mainly fills aux[M][N]
# such that aux[i][j] stores sum
# of elements from (0,0) to (i,j)
def preProcess(mat, aux):
	
	# Copy first row of mat[][] to aux[][]
	for i in range(0, N, 1):
		aux[0][i] = mat[0][i]

	# Do column wise sum
	for i in range(1, M, 1):
		for j in range(0, N, 1):
			aux[i][j] = mat[i][j] + aux[i - 1][j]

	# Do row wise sum
	for i in range(0, M, 1):
		for j in range(1, N, 1):
			aux[i][j] += aux[i][j - 1]

# A O(1) time function to compute sum of submatrix
# between (tli, tlj) and (rbi, rbj) using aux[][]
# which is built by the preprocess function
def sumQuery(aux, tli, tlj, rbi, rbj):
	
	# result is now sum of elements
	# between (0, 0) and (rbi, rbj)
	res = aux[rbi][rbj]

	# Remove elements between (0, 0)
	# and (tli-1, rbj)
	if (tli > 0):
		res = res - aux[tli - 1][rbj]

	# Remove elements between (0, 0)
	# and (rbi, tlj-1)
	if (tlj > 0):
		res = res - aux[rbi][tlj - 1]

	# Add aux[tli-1][tlj-1] as elements
	# between (0, 0) and (tli-1, tlj-1)
	# are subtracted twice
	if (tli > 0 and tlj > 0):
		res = res + aux[tli - 1][tlj - 1]

	return res

# Driver Code
if __name__ == '__main__':
	mat = [[0,1,0,0,0,0],
		[0,0,0,0,0,0],
		[1,0,0,1,0,0],
		[0,0,1,0,0,0],
        [0,0,0,0,1,0]]
aux = [[0 for i in range(N)]
		for j in range(M)]

preProcess(mat, aux)

tli = 1
tlj = 4
rbi = 4
rbj = 1
print("Query1:", sumQuery(aux, tli, tlj, rbi, rbj))

