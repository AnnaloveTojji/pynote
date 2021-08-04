# 백준: 10871 x보다 작은 수
# method 1: 
count = int(input())
num = int((input))
arr = list(map(int, input().split()))
for i in range(count):
        if arr[i] < num:
                print(arr[i], end=" ")
                
 # method 2: 
count, num = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(count):
        if arr[i] < num:
                print(arr[i], end=" ")