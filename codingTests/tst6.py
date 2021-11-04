def solution(location, s, e):
    answer = 0
    
    t=max(s[1],e[1]) #4
    b=min(s[1],e[1]) # 1
    l=min(s[0],e[1]) #1
    r=max(s[0],e[1]) #4
    
    for i in range(l,r+1):
        for j in range(b,t+1):
            if [i,j] in location:
                answer+=1
    
    

    return answer