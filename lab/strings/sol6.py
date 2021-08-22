#bj 1316: group word checker
# method1

# method2: slicing
n=int(input())
for j in range(n):
    word=input()
    for i in range(len(word)-1):
        if word[i]!=word[i+1]:
            if word[i] in word[i+1:]:
                n-=1
                break
print(n)

n = int(input())
for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] in word[i+1:]:
            n = n-1
            print("not a group word:%s"%(word))
            break
print(n)