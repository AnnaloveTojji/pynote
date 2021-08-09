# bj2577: 숫자의 개수

# solution 1: using 'count' method

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))

# solution 2: using set
