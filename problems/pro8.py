def solution(numbers):
    answer = '' 
    numbers2 = [str(n)*3 for n in numbers] # 한줄 반복문을 통해 모든 원소들의 길이를 3 곱하여 새 배열 생성
    numbers3 = list(enumerate(numbers2)) # 각 원소에 enumerate 함수로 인덱스 붙여줌
    numbers3.sort(key = lambda x:x[1], reverse = True) # 원소들의 값에 따라 정렬
    for index, value in numbers3: # 정렬된 인덱스를 이용해 차례대로 answer 만들기
        answer += str(numbers[index])
        
    return str(int(answer)) # '0000' -> 0 같은 경우를 위하여 int로 한번 바꿔주고 다시 str으로!