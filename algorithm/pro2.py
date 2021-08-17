# greedy 체육복
# abby
def sol(n, lost, reserve):
    answer = 0
    # number of items
    u = [1] *(n+2)  # initialize with 1
    # make lost 0, reserve 2
    for i in lost:
        u[i] -= 1
    for i in reserve:
        u[i] += 1
    # if the next one is lost && i am resere
    for i in range(1,n+1):
        if u[i-1] == 0 and u[i]==2:
            u[i-1]=u[i]=1
        elif u[i]==2 and u[i+1]==0:
            u[i]=i[i+1]=1
    # if item is larger than 0
    for i in range(n+1):
        if u[i]>0:
            answer += 1
    return answer - 1

print(sol(5,[2,4],[3]))
print(sol(3,[3],[1]))





## other people
# def solution(n, lost, reserve):
#     answer = 0    
#     reserve2 = [r for r in reserve if r not in lost]
#     lost2 = [l for l in lost if l not in reserve]
#     for r in reserve2:
#         if r-1 in lost2:
#             lost2.remove(r-1)
#         elif r+1 in lost2:
#             lost2.remove(r+1)
#     answer = n - len(lost2)
#     return answer