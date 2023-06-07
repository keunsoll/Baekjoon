# p, m = map(int, input().split())

# room = []
# arr = []
# visited = [0 for _ in range(p)]

# for i in range(p):
#     data = list(input().split())
#     data[0] = int(data[0])
#     arr.append(data)


# def reset_first(visited):
#     global first_index
#     for i in range(len(visited)):
#         if visited[i] == 0:
#             first_index = i
#             visited[i] = 1
#             break
#     return first_index


# # first = arr[0][0]
# # room.append(arr[0])
# while True:
#     index = reset_first(visited)
#     room.append(arr[index])
#     first = room[0][0]

#     # print(index)
#     # print(room)
#     # print(first)
#     for i in range(1, len(arr)):

#         if visited[i] == 0 and first-10 <= arr[i][0] <= first+10:
#             visited[i] = 1
#             room.append(arr[i])

#     # print("------", room)
#         if len(room) == m:
#             break
#     if len(room) == m:
#         print('Started!')
#         room.sort(key=lambda x: x[1])
#         for revel, id in room:
#             print(revel, id)
#         room = []

#     else:
#         print('Waiting!')
#         room.sort(key=lambda x: x[1])
#         for revel, id in room:
#             print(revel, id)
#         room = []

#     if visited.count(1) == len(visited):
#         break

# # print(room)


p, m = map(int, input().split())
people = []
for i in range(p):
    lv, id = input().split()
    people.append([int(lv), id])

rooms = []

for lv, id in people:
    flag = False
    for i in range(len(rooms)):
        if len(rooms[i][1]) == m:
            continue

        # 들어갈 수 있는 방이 있으면 입장
        if rooms[i][0] - 10 <= lv <= rooms[i][0] + 10:
            flag = True
            rooms[i][1].append([lv, id])
            break

    # 대기방에 들어 갈 수 없으면 새로운 방 생성
    if not flag:
        rooms.append([lv, [[lv, id]]])
# print(rooms)
# 방이 생성된 시간 순서로 출력
for i in range(len(rooms)):
    if len(rooms[i][1]) == m:
        print('Started!')
        ans = sorted(rooms[i][1], key=lambda x: x[1])
        print(ans)
        for j in range(m):
            print(*ans[j], sep=' ')
    else:
        print('Waiting!')
        ans = sorted(rooms[i][1], key=lambda x: x[1])
        for i in range(len(ans)):
            print(*ans[j])
