# O(n) solution in Python3 for finding
# maximum sum of a subarray of size k

# Returns maximum sum in
# a subarray of size k.
def maxSum(estimates, k):

	
	# window of size k
	res = 0
	for i in range(k):
		res += estimates[i]

	# Compute sums of remaining windows by
	# removing first element of previous
	# window and adding last element of
	# current window.
	curr_sum = res
	for i in range(k, len(estimates)):
	
		curr_sum += estimates[i] - estimates[i-k]
		res = max(res, curr_sum)

	return res

#Driver code
estimates = [5, 1, 9, 8, 10, 5]
k = 3
n = len(arr)
print(maxSum(arr, k))

# This code is contributed by Anant Agarwal.
