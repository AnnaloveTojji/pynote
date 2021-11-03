# naver -3
# 학생이 맞힌 문제 번호와 부분 점수가 주어질 때, 부정행위를 한 학생의 학번
def solution(logs):
    answer = []
    lst = []
    for i in logs:
        lst.append(list(i.split()))
    students = []
    problems = []
    memo = []
    for i in lst:
        students.append(i[0])  # 학생 set
        problems.append(i[1])  # 문제 set
    students = list(set(students))
    problems = list(set(problems))
    for i in students:
        d = {}
        for j in lst:
            if j[0] == i:
                d[j[1]] = j[2]
        memo.append(d)
        
        
            
    _len = len(students)
    for i in range(_len):
        for j in range(i+1,_len):
            d1=set(memo[i].keys())
            d2=set(memo[j].keys())
            if d1 & d2:
                for d in list(d1.intersection(d2)):
                    if memo[i][d]==memo[j][d] and len(memo[i])>4 and len(memo[j])>4:
                        answer.append(students[i])
                        answer.append(students[j])
    

    if len(answer) == 0: return ["None"]
    answer = sorted(list(set(answer)))
    return answer

    '''
    ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]
    '''