from collections import deque
n, m = map(int, input().split())

box = []
for i in range(n):
    box.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = []


def bfs():
    visited = [[0]*m for i in range(n)]  # 한 시간 지날 때마다 갱신
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):  # 상하좌우 확인
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                # 치즈가 아닌 부분
                if box[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])  # 큐에 추가
                # 치즈인 부분
                elif box[nx][ny] == 1:
                    visited[nx][ny] = 1
                    box[nx][ny] = 0
                    cnt += 1
    res.append(cnt)
    return cnt


time = 0
while True:
    cnt = bfs()
    time += 1
    if cnt == 0:
        break

print(time-1)
# print(res)
print(res[-2])
