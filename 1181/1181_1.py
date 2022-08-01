n=int(input())

arr=[]
for i in range(n):
    arr.append(input())

ans=list(set(arr))
#arr=list(ans)
#print(ans)
ans.sort()
ans.sort(key=len)

for i in ans:
    print(i)
