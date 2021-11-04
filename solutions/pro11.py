#큰수만들기-greedy

def solution(number, k):
    collected = [] # mutable
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
        print(i, collected) # log the process

    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer
    
print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
