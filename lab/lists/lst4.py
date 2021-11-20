# 문제1
# 첫번째 원소를 answer_1 에 할당하시오
lst = [11, 100, 99, 1000, 999]
answer_1 = lst[0]
print(answer_1)
# 문제2
# 이번에는 두번째원소를 출력. 직접적으로 print함수안에서출력
lst = [11, 100, 99, 1000, 999]
print(lst[1])
# 문제3
# 마지막 원소 출력. 힌트: 음수인덱스
lst = [11, 100, 99, 1000, 999, 1001]
answer_1 = lst[-1]
print(answer_1)
#문제4
# 리스트에다가 .append()를 사용해서 원소 "pajamas"를 추가하시오
gift_list = ['socks','4k drone','wine','jam']
gift_list.append('pajamas')
print(gift_list)
#문제5
# 리스트 인덱스3에다가 'slippers'를 insert하시오.
gift_list = ['socks','4k drone','wine','jam']
gift_list.insert(3,'slippers')
print(gift_list)
#문제6
#  .index() 메소드를 이용해서 8679의 인덱스를 answer_1 변수에 할당하시오.
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
answer_1 = lst.index(8679)
print(answer_1) #8

#문제7
# .append()를 이용하여 'e','f' 을 포함한 리스트를 추가하시오
lst=["a", "b", "c", "d"]
#lst.append(["e","f"])
lst.extend(["e","f","g"])
print(lst)

#문제8
# .remove메소드를 사용해서 마지막 원소를 지우시오.
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst.remove(99)
print(lst)


#문제9
# .reverse()를 사용해서 리스트를 거꾸로 뒤집으시오.
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst.reverse()
print(lst)

#문제10
# .count() 메소드를 사용해서 6이 몇번나오는지 세어서 출력하시오.
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1 = lst.count(6)
print(answer_1)

#문제11
# 리스트의 모든 원소를 합하여서 출력하시오 (sum)
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1 = sum(lst)
print(answer_1)


#문제11
# 리스트에서 가장 큰 원소와 가장 작은 원소를 출력하시오
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_1 = max(lst)
answer_2 = min(lst)
print(answer_1)
print(answer_2)








