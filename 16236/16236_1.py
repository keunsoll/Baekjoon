from collections import deque
n = int(input())

space = []
for i in range(n):
    space.append(list(map(int, input().split())))

# 아기 상어 크기
baby = 2
# 아기 상어 위치
for i in range(len(space)):
    if 9 in space[i]:
        point = [i, space[i].index(9)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 참고
def bfs(i, j, baby):
    distance = [[0]*n for i in range(n)]
    visited = [[0]*n for i in range(n)]

    q = deque()
    q.append((i, j))

    visited[i][j] = 1
    temp = []

    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx = dx[i]+xx
            ny = dy[i]+yy

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if space[nx][ny] <= baby:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[xx][yy]+1  # 거리 증가

                    if space[nx][ny] < baby and space[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))
    # 거리가 가까운 물고기가 많을 시, 가장 위에 있는 물고기, 가장 왼쪽에 있는 물고기 순
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


res = 0
cnt = 0
while True:
    shark = bfs(point[0], point[1], baby)

    # 더 이상 먹을 수 있는 물고기 없을 때
    if len(shark) == 0:
        break
    nx, ny, dist = shark.pop()

    # 거리 합산
    res += dist
    space[point[0]][point[1]], space[nx][ny] = 0, 0

    # 좌표 옮기기
    point[0], point[1] = nx, ny
    cnt += 1

    if cnt == baby:
        baby += 1
        cnt = 0

print(res)
