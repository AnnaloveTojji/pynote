#bj4344: 평균은 넘겠지
a = int(input())
for _ in range(a):
    count = 0
    arr = list(map(int, input().split()))
    avg = (sum(arr)-arr[0])/arr[0] #sum(arr)-arr[0] == sum(arr[1:])
    for i in arr[1:]:
        if i > avg:
            count+=1
    r = count/arr[0]*100
    print(f"{r:.3f}%")