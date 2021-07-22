#tuples - exercises

# ex1
# unpack a tuple in variables, and print the sum of all 
tuplex = 4, 8, 3
# answer here


# ex1 - solution
#create a tuple
tuplex = 4, 8, 3 
print(tuplex)
n1, n2, n3 = tuplex
#unpack a tuple in variables
print(n1 + n2 + n3) 


# ex2
# add an item to a tuple
tuplex = (1, 2, 3, 4) 
# expected output: (1, 2, 3, 100, 200, 300, 1, 2, 3)
# answer here



# ex2 - solution
#create a tuple
tuplex = (1, 2, 3, 4) 
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#adding items in a specific index
tuplex = tuplex[:3] + (100, 200, 300) + tuplex[:3]
print(tuplex)


# ex3
# convert a tuple to a list and append an element 
tuplex = (1, 2, 3, 4) 
# expected output:(1, 2, 3, 4, 100)
# answer here


# ex3 - solution
tuplex = (1, 2, 3, 4) 
listx = list(tuplex) 
listx.append(100)
tuplex = tuple(listx)
print(tuplex)


# ex4
# count the number of 100 in a tuple
tuplex = 2, 100, 5, 6, 2, 3, 100, 100, 7 
# expected output: 3
# answer here


# ex4 - solution(1)
tuplex = 2, 100, 5, 6, 2, 3, 100, 100, 7 
count = tuplex.count(4)
print(count)

# ex4 - solution(2)
tuplex = 2, 100, 5, 6, 2, 3, 100, 100, 7 
cnt = 0
for x in tuplex:
    if x == 100:
        cnt += 1
print("the number of 100: %d"% cnt)


