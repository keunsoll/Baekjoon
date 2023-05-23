p = int(input())

for i in range(p):
    data = list(map(int, input().split()))
    t = data[0]
    height = [data[i] for i in range(1, len(data))]

    cnt = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            if height[i] > height[j]:
                height[i], height[j] = height[j], height[i]

                cnt += 1
        print(height)
    print(height)
    print(t, cnt)
