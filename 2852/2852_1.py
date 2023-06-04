n = int(input())

end = 48*60  # 초로 변경
cnt = 0

t1 = 0
t2 = 0

for i in range(n):
    team, goal_time = input().split()
    minute, sec = map(int, goal_time.split(":"))
    time = minute*60 + sec

    if team == '1':
        if cnt == 0:
            t1 += (end-time)
        cnt += 1
        if cnt == 0:
            t2 -= (end - time)

    else:
        if cnt == 0:
            t2 += (end-time)
        cnt -= 1
        if cnt == 0:
            t1 -= (end - time)


def _print(num):
    if len(num) == 1:
        num = "0"+num
    return num


print(_print(str(t1//60)) + ':' + _print(str(t1 % 60)))
print(_print(str(t2//60)) + ':'+_print(str(t2 % 60)))
