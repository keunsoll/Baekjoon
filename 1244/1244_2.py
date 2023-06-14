
n = int(input())
switch = [-1]+list(map(int, input().split()))
sn = int(input())


def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0


for i in range(sn):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(num, len(switch)):
            if i % num == 0:
                change(i)
    else:

        for i in range(n//2):
            if num-i < 1 or num+i > n:
                break
            else:
                if switch[num-i] == switch[num+i]:
                    change(num-i)
                    change(num+i)
                else:
                    break
        change(num)

for i in range(1, len(switch)):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()
