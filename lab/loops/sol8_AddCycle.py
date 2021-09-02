# #더하기 사이클

num = int(input())
init = num
new_num = 0
count = 0
while True:
    #temp = num//10 + num%10
    new_num = (num%10)*10 + (num//10 + num%10)%10
    count += 1
    num = new_num
    if new_num == init:
        break
print(count)

# x = int(input())
# if x<10:
#     x*=10
# y=0
# cnt=0
# while True:
#     a = x/10
#     b = x%10
#     c = a+b
#     y=b*10+c
#     cnt += 1
#     if x==y:
#         break
#     x=y
#
# print(cnt)
#