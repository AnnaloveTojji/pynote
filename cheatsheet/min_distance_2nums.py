# Python3 code to Find the minimum
# distance between two numbers


def minDist(arr, n, x, y):
	min_dist = 99999999
	for i in range(n):
		for j in range(i + 1, n):
			if (x == arr[i] and y == arr[j] or
					y == arr[i] and x == arr[j]) and min_dist > abs(i-j):
				min_dist = abs(i-j)
		return min_dist


# Driver code
arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
n = len(arr)
x = 3
y = 6
print(minDist(arr, n, x, y))


################################
# This code is contributed by "Abhishek Sharma 44"

import sys

def minDist2(arr, n, x, y):
	
	#previous index and min distance
	i=0
	p=-1
	min_dist = sys.maxsize;
	
	for i in range(n):
	
		if(arr[i] ==x or arr[i] == y):
		
			#we will check if p is not equal to -1 and
			#If the element at current index matches with
			#the element at index p , If yes then update
			#the minimum distance if needed
			if(p != -1 and arr[i] != arr[p]):
				min_dist = min(min_dist,i-p)
			
			#update the previous index
			p=i
		
	
	#If distance is equal to int max
	if(min_dist == sys.maxsize):
		return -1
	return min_dist


# Driver program to test above function */
arr = [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3]
n = len(arr)
x = 3
y = 6
print (minDist2(arr, n, x, y))

# This code is contributed by Shreyanshi Arun.
