#naver-1
# 쿠폰 지급, 하루 최대 1개, 쿠폰의 총 지급 개수

def solution(id_list, k):
    answer = 0
    lst=[]
    for i in id_list:
        lst += list(set(list(i.split())))
    print(lst)
    keys=list(set(lst))
    print(keys)
    for i in keys:
        if lst.count(i)>=k:
            answer+=k
        else:
            answer+=lst.count(i)
    return answer

print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"],3))
#print(solution(["A B C D", "A D", "A B D", "B D"],2))