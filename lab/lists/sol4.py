#bj1546: 평균
a = int(input())
score_list = list(map(int, input().split()))
max = max(score_list)
result = 0
 
for i in range(0, a):
    score_list[i] = score_list[i]/max*100
    result = result + score_list[i]
 
result = result/a
print(result)