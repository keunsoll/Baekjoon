h, w = map(int, input().split())

for i in range(h):
    data = list(input())

    time = []
    cnt = 0
    for j in range(w):
        if data[j] == 'c':
            cnt = 0
            time.append(cnt)

        else:
            if 'c' in data[:j]:
                cnt += 1
                time.append(cnt)
            else:
                time.append(-1)

    for j in time:
        print(j, end=" ")
