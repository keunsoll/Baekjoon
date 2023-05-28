n = int(input())

arr = []
ans = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    cnt = 1
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    ans.append(cnt)

    # print(arr)
# print(ans)
for i in ans:
    print(i)
