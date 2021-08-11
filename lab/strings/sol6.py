#bj 1316: group word checker
# method1

# method2: slicing
n=int(input())
cnt=0
for j in range(n):
    word=input()
    for i in range(len(word)-1):
        if word[i]!=word[i+1]:
            if word[i] in word[i+1:]:
                n-=1
                break
print(n)
