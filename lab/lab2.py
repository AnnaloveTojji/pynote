#loops 

#using 'for' - print a christmas tree 
print("*** 'for' tree ***")
for x in range(1, 6):
    print(' '* (5 - x) + '*' * ( x * 2 - 1))


#using 'while' - print a christmas tree
print("*** 'while' tree ***")
i=1
while i<6:
    print(' '* (5 - i) + '*' * ( i * 2 - 1))
    i += 1

#get an input for the tree size
print("*** tree with user input ***")
n = int(input("Please enter an integer:"))
for x in range(1, n +1):
    print(' '* (n - x) + '*' * ( x * 2 - 1))


