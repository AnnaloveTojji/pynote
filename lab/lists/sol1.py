#bj 10818: min, max

n = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]
for i in numbers:
    if i > max:
        max = i
    if i < min:
        min = i
print(min, max)