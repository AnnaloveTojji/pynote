#bj1546: 평균
# a = int(input())
# score_list = list(map(int, input().split()))
# max = max(score_list)
# result = 0
 
# for i in range(0, a):
#     score_list[i] = score_list[i]/max*100
#     result = result + score_list[i]
 
# result = result/a
# print(result)

# 1. get input: num of subjects, score..
n = int(input("enter the number of subjects: "))
score_list = list(map(int,input("enter the scores: ").split()))
# 2. find the max
m = max(score_list)
print(m)
# 3. 고친다: 모든score / m * 100 ->모든 점수.
for i in range(n): # 0~n-1
    score_list[i] = score_list[i] / m * 100
# 4.  새로운 평균.. sum/num
print(sum(score_list)/n)