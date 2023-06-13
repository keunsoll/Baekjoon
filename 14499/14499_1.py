### 입력 ###
n, m, x, y, k = map(int, input().split())

mmap = []
for i in range(n):
    mmap.append(list(map(int, input().split())))

command = list(map(int, input().split()))
##########

### 주사위 굴리기 ###
dice = [0, 0, 0, 0, 0, 0]


def turn_dice(direction):
    top, back, right, left, front, bottom = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:  # 동
        dice[0], dice[2], dice[3],  dice[5] = left,  top, bottom,  right
    elif direction == 2:  # 서
        dice[0],  dice[2], dice[3],  dice[5] = right, bottom, top, left
    elif direction == 3:  # 북
        dice[0], dice[1],  dice[4], dice[5] = front, top, bottom, back
    else:  # 남
        dice[0], dice[1],  dice[4], dice[5] = back, bottom, top, front
##########


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

nx, ny = x, y
for i in command:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue

    turn_dice(i)
    if mmap[nx][ny] == 0:
        mmap[nx][ny] = dice[-1]  # 칸에 주사위 바닥면 복사
    else:
        dice[-1] = mmap[nx][ny]  # 주사위 바닥면에 칸 숫자 복사
        mmap[nx][ny] = 0  # 칸 숫자를 0으로

    print(dice[0])
