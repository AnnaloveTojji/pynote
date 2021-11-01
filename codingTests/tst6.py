# Python3 program for the above approach
# Function to prthe maximum rooks
# and their positions
def countRooks(n, k, pos):
	
	row = [0 for i in range(n)]
	col = [0 for i in range(n)]

	# Marking the location of
	# already placed rooks
	for i in range(k):
		row[pos[i][0] - 1] = 1
		col[pos[i][1] - 1] = 1

	res = n - k

	# Print number of non-attacking
	# rooks that can be placed
	print(res)

	# To store the placed rook
	# location
	ri = 0
	ci = 0
	
	while (res > 0):

		# Print lexographically
		# smallest order
		while (row[ri] == 1):
			ri += 1
			
		while (col[ci] == 1):
			ci += 1
			
		print((ri + 1), (ci + 1))
		
		ri += 1
		ci += 1
		res -= 1

# Driver Code
if __name__ == '__main__':

	# Size of board
	N = 4

	# Number of rooks already placed
	K = 2

	# Position of rooks
	pos= [ [ 1, 4 ], [ 2, 2 ] ]

	# Function call
	countRooks(N, K, pos)

# This code is contributed by mohit kumar 29
