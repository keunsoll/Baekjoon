n, m = map(int, input().split())
t = list(map(int, input().split()))
t.sort()

first = t[0]
third = t[2]


for i in range(first, third+1):
    arr = 0
    for j in range(len(t)-2):
        arr += t[j+2]-i
        if arr == m:
            print(i)
            break
