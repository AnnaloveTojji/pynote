

# method1: recursion
# Python code to demonstrate naive
# method to compute gcd ( recursion )

def hcfnaive(a,b):
	if(b==0):
		return a
	else:
		return hcfnaive(b,a%b)

a = 60
b= 48

# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (hcfnaive(60,48))


# method2: loops
# Python code to demonstrate naive
# method to compute gcd ( Loops )


def computeGCD(x, y):

	if x > y:
		small = y
	else:
		small = x
	for i in range(1, small+1):
		if((x % i == 0) and (y % i == 0)):
			gcd = i
			
	return gcd

a = 60
b= 48

# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60,48))

# method3: euclidean
# Python code to demonstrate naive
# method to compute gcd ( Euclidean algo )


def computeGCD(x, y):

while(y):
	x, y = y, x % y

return x

a = 60
b= 48

# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60,48))


# method4: module math
# Python code to demonstrate gcd()
# method exceptions

import math

# prints 0
print ("The gcd of 0 and 0 is : ",end="")
print (math.gcd(0,0))

# Produces error
print ("The gcd of a and 13 is : ",end="")
print (math.gcd('a',13))
