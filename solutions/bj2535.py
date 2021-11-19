#bj 2535
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

