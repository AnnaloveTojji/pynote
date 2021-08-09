# how to get multiple inputs in a line
# method 1

x, y = input(),  input()

# method 2

x, y = input().split()

# Reads two numbers from input and typecasts them to int using
# list comprehension
x, y = [int(x) for x in input().split()]

# Reads two numbers from input and typecasts them to int using
# map function
x, y = map(int, input().split())
