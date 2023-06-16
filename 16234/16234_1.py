from collections import deque
n, l, r = map(int, input().split())

land = []
for i in range(n):
    land.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    union = []
    union.append([i, j])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(land[nx][ny]-land[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    union.append([nx, ny])
    return union


cnt = 0
while True:
    visited = [[0]*n for _ in range(n)]
    check = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union = bfs(i, j)
                # 인구 이동
                if len(union) > 1:
                    check = 1
                    num = sum(land[x][y] for x, y in union)//len(union)
                    for x, y in union:
                        land[x][y] = num
    # 인구 이동 x
    if check == 0:
        break
    cnt += 1
print(cnt)
