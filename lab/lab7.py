# lists: exercises-basic

# ex1
# sum every element in a list
list1 = [1, 100, 200, -200]
# answer here

# ex1-solution
list1 = [1, 100, 200, -200]
sum = 0
for x in list1:
    sum += x
print(sum)

# ex2
# multiply every element in a list
list1 = [1, 2, -8]
# answer here


#ex2-solution
list1 = [1, 2, -8]
tot = 1
for x in list1:
    tot *= x
print(tot)

# ex3
# get the largest number from a list
list1 = [1, 2, -8, 0]
# answer here


#ex3-solution
list1 = [1, 2, -8, 0]
max = list1[ 0 ]
for x in list1:
    if x > max:
        max = x
print(max)

# ex4
# print True if two lists have at least one common member
list1 = [1,2,3,4]
list2 = [3,4,5,6]
# answer here


#ex4-solution
list1 = [1,2,3,4]
list2 = [3,4,5,6]
for x in list1:
    for y in list2:
        if x == y:
            print(True)
        break

# ex5
# count the number of common members in two lists
list1 = [1,2,3,4]
list2 = [3,4,5,6]
# answer here


#ex5-solution
list1 = [1,2,3,4]
list2 = [3,4,5,6]
cnt = 0
for x in list1:
    for y in list2:
        if x == y:
            cnt += 1
print(cnt)
