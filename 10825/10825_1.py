n=int(input())
std=[]

for i in range(n):
    std.append(input().split())

std.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# sort(key=lambda x: 차례대로 입력된 인자들의 인덱스 기준으로 정렬
for i in std:
    print(i[0])

