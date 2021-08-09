#백준 2675: 문자열 반복
t = int(input("t: "))
for i in range(t):
        r, s = input().split()
        r = int(r)
        for j in range(r):
            res = s[j]*3
            print(res, end='')
        print()