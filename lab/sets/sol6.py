# 백준 2577: 숫자의 개수
nums = set()  
for _ in range(10):
    i = int(input())
    nums.add(i%42)  
print(len(nums))