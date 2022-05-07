m, d = map(int, input().split())

b_month = [1, 3, 5, 7, 8, 10, 12]
n_month = [4, 6, 9, 11]
s_month = [2]

day = 0
for i in range(1, m):
    if i in b_month:
        day += 31
    elif i in n_month:
        day += 30
    elif i in s_month:
        day += 28
day += d

if day % 7 == 0:
    print("SUN")
elif day % 7 == 1:
    print("MON")
elif day % 7 == 2:
    print("TUE")
elif day % 7 == 3:
    print("WED")
elif day % 7 == 4:
    print("THU")
elif day % 7 == 5:
    print("FRI")
elif day % 7 == 6:
    print("SAT")
