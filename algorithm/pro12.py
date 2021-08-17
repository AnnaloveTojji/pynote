# bj11399 : atm
n = int(input("n: "))
p = list(map(int, (input("p: ").split())))
p.sort()
sum = 0
for i in range(n):
    for j in range(i + 1):
        sum += p[j]
print(sum)
