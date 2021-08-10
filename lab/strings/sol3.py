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


# method 2: dict
# word = input().upper()
# alphabet = {}

# for i in word:
#     if i in alphabet:
#         alphabet[i] += 1

# res = 0
# max = 0

# for i in alphabet:
#     if alphabet[i] > max:
#         max = alphabet[i]
#         res = i
#     elif alphabet[i] == max:
#         res = '?'

# print(res)