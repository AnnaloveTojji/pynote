# 백준 1157: 단어공부
# method 1: list, set
n = input().upper()
keys = list(set(n))
 
countArr = []
for k in keys:
    countArr.append(n.count(k))
 
if countArr.count(max(countArr)) > 1:
    print("?")
else:
    print(keys[countArr.index(max(countArr))])

