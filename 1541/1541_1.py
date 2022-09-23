str = input().split('-')

n = []
for i in str:
    num = 0
    plus = i.split('+')
    # print(plus)
    for j in plus:
        num += int(j)
    n.append(num)
    # print(n)

ans = n[0]
for i in range(1, len(n)):
    ans -= n[i]
print(ans)
