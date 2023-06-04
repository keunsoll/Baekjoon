n = int(input())
switch = [-1]+list(map(int, input().split()))
sn = int(input())
# print(switch)


def change(num):
    if switch[num] == 1:
        switch[num] = 0
    else:
        switch[num] = 1


def woman(num):
    for i in range(n//2):
        if num-i < 1 or num+i > n:
            break
        else:
            if switch[num-i] == switch[num+i]:
                change(num-i)
                change(num+i)

            else:
                break


for i in range(sn):
    gender, num = map(int, input().split())

    if gender == 1:
        for j in range(num, len(switch)):
            if j % num == 0:
                change(j)
    elif gender == 2:
        change(num)
        woman(num)

for i in range(1, len(switch)):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()
