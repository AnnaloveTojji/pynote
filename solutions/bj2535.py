#bj 2535

# solution1

lst =[]
n =int(input())
for i in range(n):
    x,y,score=map(int,input("x,y,score: ").split())
    lst.append([x,y,score])
lst.sort(key=lambda x: (x[2],x[0]), reverse=True)
cntlist = [0]*n
count = 0

for i in lst:
    if count > 2:
        break
    else:
        idx = i[0]
        cntlist[idx] += 1
        if cntlist[idx] < 3:
            print (i[0], i[1])
            count += 1

# wrong way!
n =int(input())
nlist = [input().split() for i in range(n)]
nlist.sort(key=lambda x: -int(x[2]))

print("**log",nlist)

count = 2
if nlist[0][0] == nlist[1][0]:
    while nlist[0][0] == nlist[count][0]:
        count += 1
        print("**log",count)
for i in (0,1,count):
    print(nlist[i][:2])
    


