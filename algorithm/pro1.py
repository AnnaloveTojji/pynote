# heap-완주하지 못한선수
# abby
def solution(participant, completion):
    ans = ""
    d = {} #empty dictionary
    d ={participant: [] for participant in range(4)}
    for i in participant:
        d[i] +=1
    for i in completion:
        d[i] -=1
    for i in d:
        if i.values > 0:
            ans = i.keys
            break
    return ans


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
["josipa", "filipa", "marina", "nikola"]))

# others
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for p,c in zip(participant, completion):
#         if p != c:
#             return p
#     return participant.pop()