# n으로 표현 -dp
def solution(N, number):
    s = [set() for x in range(8)]
    for i, x in enumerate(s, start=1):
        x.add(int(str(N)*i))
    for i in range(len(s)): #버그 수정
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op1 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer

        
print(solution(5, 12)) #4
print(solution(2, 11)) #3