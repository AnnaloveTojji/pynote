# Python program to find Minimum number of
# subsets with distinct elements using Counter

# function to find Minimum number of subsets
# with distinct elements
from collections import Counter

def minSubsets(input):

	# calculate frequency of each element
	freqDict = Counter(input)

	# get list of all frequency values
	# print maximum from it
	print (max(freqDict.values()))

# Driver program
if __name__ == "__main__":
	input = [1, 2, 3, 3]
	minSubsets(input)
