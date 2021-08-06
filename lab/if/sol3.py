#백준 2884: 알람시계

# method 1: using two inputs

hour = int(input("Enter the hour: "))
minute = int(input("Enger the minute: "))

if minute > 44:
    print(hour, minute-45)
elif hour >= 1:
    print(hour-1, minute+15)
else:
    print(23, minute+15)

# method 2: using maps
hour,minute = map(int, input().split())

if minute > 44:
    print(hour, minute-45)
elif hour >= 1:
    print(hour-1, minute+15)
else:
    print(23, minute+15)