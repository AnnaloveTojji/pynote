'''
자연수 N개가 중복없이 들어있는 배열이 있습니다. 이때, 서로 다른 두 원소의 위치를 바꾸는 Swap 연산을 이용해 원소들의 위치를 바꿔 서로 인접한 원소의 차가 K 이하가 되도록 하려 합니다. 단, Swap 연산을 최대한 적게 사용해야 합니다
'''
# Python3 program for the above approach

# Function to find the minimum number
# of swaps required to sort the array
# in increasing order
def minSwapsAsc(arr, n):
	
	# Stores the array elements with
	# its index
	arrPos = [[arr[i], i] for i in range(n)]

	# Sort the array in the
	# increasing order
	arrPos = sorted(arrPos)

	# Keeps the track of
	# visited elements
	vis = [False] * (n)

	# Stores the count of swaps required
	ans = 0

	# Traverse array elements
	for i in range(n):
		
		# If the element is already
		# swapped or at correct position
		if (vis[i] or arrPos[i][1] == i):
			continue

		# Find out the number of
		# nodes in this cycle
		cycle_size = 0

		# Update the value of j
		j = i

		while (not vis[j]):
			vis[j] = 1

			# Move to the next element
			j = arrPos[j][1]

			# Increment cycle_size
			cycle_size += 1

		# Update the ans by adding
		# current cycle
		if (cycle_size > 0):
			ans += (cycle_size - 1)

	return ans

# Function to find the minimum number
# of swaps required to sort the array
# in decreasing order
def minSwapsDes(arr, n):
	
	# Stores the array elements with
	# its index
	arrPos = [[0, 0] for i in range(n)]

	for i in range(n):
		arrPos[i][0] = arr[i]
		arrPos[i][1] = i

	# Sort the array in the
	# descending order
	arrPos = sorted(arrPos)[::-1]

	# Keeps track of visited elements
	vis = [False] * n

	# Stores the count of resultant
	# swap required
	ans = 0

	# Traverse array elements
	for i in range(n):
		
		# If the element is already
		# swapped or at correct
		# position
		if (vis[i] or arrPos[i][1] == i):
			continue

		# Find out the number of
		# node in this cycle
		cycle_size = 0

		# Update the value of j
		j = i

		while (not vis[j]):
			vis[j] = 1

			# Move to the next element
			j = arrPos[j][1]

			# Increment the cycle_size
			cycle_size += 1

		# Update the ans by adding
		# current cycle size
		if (cycle_size > 0):
			ans += (cycle_size - 1)
			
	return ans

# Function to find minimum number of
# swaps required to minimize the sum
# of absolute difference of adjacent
# elements
def minimumSwaps(arr):
	
	# Sort in ascending order
	S1 = minSwapsAsc(arr, len(arr))

	# Sort in descending order
	S2 = minSwapsDes(arr, len(arr))

	# Return the minimum value
	return min(S1, S2)

# Drive Code
if __name__ == '__main__':
	
	arr = [3, 7, 2, 8, 6, 4, 5, 1]
	print (minimumSwaps(arr))
    
# This code is contributed by mohit kumar 29
