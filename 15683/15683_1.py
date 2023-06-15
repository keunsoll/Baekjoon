# 참고
import copy
n, m = map(int, input().split())
cctv = []  # cctv 번호, 좌표
mode = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], [[0, 1, 2, 3]],
        ]  # 각 cctv의 방향정보

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


room = []
for i in range(n):
    arr = list(map(int, input().split()))
    room.append(arr)
    for j in range(m):
        if arr[i] in [1, 2, 3, 4, 5]:
            cctv.append([arr[i], i, j])


def watch(room, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if room[nx][ny] == 6:
                break
            elif room[nx][ny] == 0:
                room[nx][ny] = -1


def dfs(depth, room):
    global mmin
    if depth == len(cctv):  # 탐색 완
        cnt = 0
        for i in range(n):
            cnt += room[i].count(0)
        mmin = min(mmin, cnt)
        return
    room_ = copy.deepcopy(room)  # 복제
    n_cctv, x, y = cctv[depth]  # 탐색할 cctv
    for i in mode[n_cctv]:
        watch(room_, i, x, y)  # 방향에 따라
        dfs(depth+1, room_)
        room_ = copy.deepcopy(room)  # 초기화


mmin = int(1e9)
dfs(0, room)
print(mmin)
