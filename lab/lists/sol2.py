# 백준10871:  x보다 작은수
# input
n, x = map(int,input("n, x: ").split())
A = list(map(int,input("list A: ").split()))
for i in range(n):
    if A[i] < x:
        print(A[i], end=" ")