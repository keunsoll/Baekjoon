import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

room = []
for i in range(n):
    room.append(list(map(int, input().split())))

visit = [[0]*m for i in range(n)]
visit[x][y] = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check():
    global d
    d -= 1
    if d == -1:
        d = 3


cnt = 1
rotate_cnt = 0
while True:
    check()

    nx = x+dx[d]
    ny = y+dy[d]

    # 청소해야하는 칸
    if room[nx][ny] == 0 and visit[nx][ny] == 0:
        visit[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        rotate_cnt = 0
        continue
    else:
        rotate_cnt += 1
    if rotate_cnt == 4:
        nx = x-dx[d]
        ny = y-dy[d]
        # 뒤로 갈 수 있다면
        if room[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        rotate_cnt = 0

print(cnt)
