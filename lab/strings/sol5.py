# bj 2908: reverse numbers

# method1: string slicing
num = input()
print(str(num)[::-1])

# method2: loop
s = input()
reversedString=[]
index = len(s) 
while index > 0: 
    reversedString += s[ index - 1 ] 
    index = index - 1 
print(reversedString) 