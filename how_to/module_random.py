import random
# random
print(random.random())

# random, no duplicates
random.sample(range(100), 10)

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