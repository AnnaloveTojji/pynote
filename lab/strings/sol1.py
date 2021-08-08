# 백준 10809: 알파벳 찾기   
# https://www.acmicpc.net/problem/10809

s = input()
alphabet = list(range(97, 123)) # 아스키코드 알파벳 소문자 범위

for x in alphabet:
    print(s.find(chr(x)), end=" ")