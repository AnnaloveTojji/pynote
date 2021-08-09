import random
import time

words = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]

n = 1
print("Press 'enter' to start!")
input()
start = time.time()

question = random.choice(words)

while n <= 5:
    print("-- word #{} --".format(n))
    print(question)
    answer = input()

    if (question == answer):
        print("** Success! **")
        n = n+1
        question = random.choice(words)

    else :
        print("** Fail! **")

end = time.time()
et = end - start
et = format(et, ".2f")
print("time :", et, "seconds")