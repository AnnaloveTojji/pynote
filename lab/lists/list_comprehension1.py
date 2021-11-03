'''
list comprehension - syntax
newlist = [expression for item in iterable if condition == True]
'''

# for loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#condition
newlist = [x for x in fruits if x != "apple"]

# iteration
newlist = [x for x in range(10)]

# expression
newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]