# lists: exercises-advanced

# ex1
# Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# write your answer here

list1[2][2].insert(2,70000)
print(list1)
print(list1)
# expected output [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# ex2
# Given a nested list extend it by adding the sub list ["h", "i", "j"] 
# in such a way that it will look like the following list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# write your answer here

print(list1)
# expected output: ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


# ex3
# Given a Python list, find value 20 in the list, 
# and if it is present, replace it with 200. 
# Only update the first occurrence of a value.
list1 = [5, 10, 15, 20, 25, 50, 20]
# write your answer here

print(list1)
# expected output: list1 = [5, 10, 15, 200, 25, 50, 20]



# ex1 - solution
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# ex2 - solution
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]

list1[2][1][2].extend(subList)
print(list1)

# ex3 - solution
list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)
list1[index] = 200
print(list1)
