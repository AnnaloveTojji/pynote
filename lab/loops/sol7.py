# aliquot sum


# Python 3 program for aliquot sum
 
# Function to calculate sum of
# all proper divisors
def aliquotSum(n) :
    sm = 0
    for i in range(1,n) :
        if (n % i == 0) :
            sm = sm + i    
     
    return sm # return sum
 
 
# Driver Code
n = 12
print(aliquotSum(n))