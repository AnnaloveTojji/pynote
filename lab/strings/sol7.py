# bj 4344: 평균은 넘겠지
c = int(input())
for _ in range(c):
    count = 0
    arr = list(map(int, input().split()))
    avg = (sum(arr)-arr[0])/arr[0] 
    for i in arr[1:]:
        if i > avg:
            count+=1
    r = count/arr[0]*100 # r: ratio
    print(f"{r:.3f}%")