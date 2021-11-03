#설탕배달
#sol1
n = int(input()) # 설탕
result = 0 # 봉지 수
while n >= 0:
    if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
        result += n // 5 # 5로 나눈 몫 추력
        print(result)
        break
    n -= 3 # 설탕이 5의 배수가 될때까지 반복
    result += 1 # 봉지 추가
else:
    print(-1) # while문이 거짓이 되면 -1 출력

# sol2
inp = int(input())
Box = 0
while True:
    if inp % 5 == 0:
        Box = Box + inp//5
        print(Box)
        break
    inp = inp-3
    Box += 1
    if inp < 0:
        print("-1")
        break

#sol3
import sys
read = sys.stdin.readline
N = int(read())
arr = [5001] * (N+5)
arr[3] = arr[5] = 1
for i in range(6, N+1): 
    arr[i] = min(arr[i-3], arr[i-5]) + 1
print(arr[N] if arr[N] < 5001 else -1)