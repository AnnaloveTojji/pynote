# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))



# initialize sum and counter
sum = 0
i = 1
while i < 11:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

i = 0
while i < 3:
    print(i)
    i = i + 1

'''Example to illustrate
the use of else statement
with the while loop'''

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")