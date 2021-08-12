#백준 2675: 문자열 반복
t = int(input("t: "))
for i in range(t):
    r, s = input().split()
    r = int(r)
    s = list(s)
    for j in s:
        print(j*r,end='')

