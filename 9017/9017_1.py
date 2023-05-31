t = int(input())

for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    arr = []
    for j in data:
        if data.count(j) >= 6:
            arr.append(j)

    team = list(set(arr))
    rank = [[] for i in range(len(team))]

    for j in range(len(team)):
        rank[j].append(team[j])
        for k in range(len(arr)):
            if team[j] == arr[k]:
                rank[j].append((k+1))

    res = [[] for i in range(len(rank))]
    for j in range(len(rank)):
        res[j].append(rank[j][0])
        score = 0
        for k in range(1, 5):
            score += rank[j][k]
        res[j].append(score)
        res[j].append(rank[j][5])

    res.sort(key=lambda x: (x[1], x[2]))
    print(res[0][0])


# 세 가지 요소만 뽑아서 정렬
