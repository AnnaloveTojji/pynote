# 백준 10809: 알파벳 찾기   

s = input()
ascii = list(range(97, 123)) 

for i in ascii:
    print(s.find(chr(i)), end=" ")


