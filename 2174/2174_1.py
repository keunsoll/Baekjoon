# 다시
a, b = map(int, input().split())
n, m = map(int, input().split())

data = []
dir = {"N": 0, "E": 1, "S": 2, "W": 3}
command = []
graph = [[0]*(a+1) for i in range(b+1)]

for i in range(n):
    x, y, direction = input().split()
    x, y = int(x), int(y)
    data.append([i+1, x, y, dir[direction]])
    graph[y][x] = i+1  # y가 가로 x가 세로

for i in range(m):
    command.append(input().split())
    command[i][0], command[i][2] = int(command[i][0]), int(command[i][2])

# print(data)
# print(command)
# print(graph)


def turn_left(direction):  # 왼쪽 90도 회전
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


def turn_right(direction):  # 오른쪾 90도 회전
    direction += 1
    if direction == 4:
        direction = 0
    return direction


# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    for i in range(len(data)):
        check = 0
        d = data[i][3]
        xx, yy = data[i][1], data[i][2]

        comm_cnt = command[i][2]

        if command[i][1] == "L":
            for _ in range(comm_cnt):
                turn_left(d)
                nx = xx+dy[d]
                ny = yy+dx[d]
        elif command[i][1] == "R":
            for _ in range(comm_cnt):
                turn_right(d)
                nx = xx+dy[d]
                ny = yy+dx[d]
        elif command[i][1] == "F":  # 전진
            for _ in range(comm_cnt):
                nx = xx+dy[d]
                ny = yy+dx[d]
                # print(nx, ny)
                if nx <= 0 or ny <= 0 or nx > b or ny > a:
                    check = 1
                    print("Robot %d crashes into the wall" % (i+1))
                    break
                elif graph[ny][nx] != 0:
                    check = 2
                    print("Robot %d crashes into robot %d" %
                          (i+1, graph[ny][nx]))
                    break
                else:
                    xx, yy = nx, ny
                    graph[yy][xx] = i+1
        if check != 0:
            break

    if check == 0:
        print("OK")
        break
    else:
        break

