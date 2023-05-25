n, k = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

print(data)

for i in range(n):
    if data[i][0] == k:
        j = i
for i in range(n):
    if data[j][1:] == data[i][1:]:
        print(i+1)
        break
