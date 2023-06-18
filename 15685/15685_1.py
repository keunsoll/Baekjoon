# 방향
# 0세대: 0
# 1세대: 0 1
# 2세대: 0 1 2 1
# 3세대: 0 1 2 1 2 3 2 1
# 4세대: 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1


n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

curve = [[0]*101 for i in range(101)]

for i in range(n):
    x, y, d, g = map(int, input().split())
    curve[x][y] = 1

    move = [d]

    # g세대
    for _ in range(g):
        per = []
        for i in range(len(move)):
            per.append((move[-i-1]+1) % 4)  # 방향 주기
        move.extend(per)

    for j in move:
        nx = x+dx[j]
        ny = y+dy[j]
        curve[nx][ny] = 1
        x, y = nx, ny

cnt = 0
for i in range(100):
    for j in range(100):
        if curve[i][j] and curve[i+1][j] and curve[i][j+1] and curve[i+1][j+1]:
            cnt += 1
print(cnt)
