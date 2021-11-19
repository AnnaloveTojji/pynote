import random

def reply(x):
    if x == True:
        print("Correct!")
    else:
        print("Incorrect!")

# set numbers
score = 0
num1 = random.randint(1,11)
num2 = random.randint(1,11)
operators = ['+','-','*','/']
choice = random.randint(0,3)
op = operators[choice]

# ask
answer = int(input("What is %d %s %d ?"%(num1, op, num2)))

# check result
if op == "+":
    reply(answer == num1 + num2)
elif op == "-":
    pass
elif op == "*":
    pass
else:
    pass
print("**game over**")