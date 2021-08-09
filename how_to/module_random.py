import random
# random
print(random.random())

# randrange
print(random.randrange(3, 9))

# randint
print(random.randint(3, 9))

# choice
mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))

# seed
random.seed(2)

print(random.random())
print(random.random())
print(random.random())