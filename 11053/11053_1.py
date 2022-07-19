#dp
#수가 같을때가 관건

#1번째
n=int(input())

ai=list(map(int,input().split()))
ans=[0]*n

for i in range(n):
    for j in range(i):
        if ai[i]>ai[j] and ans[i]<ans[j]:
            ans[i]=ans[j]
    ans[i]+=1
print(max(ans))            

# 2번째
n=int(input())
ai=list(map(int,input().split()))
ans=[1]*n

for i in range(n):
    for j in range(i):
        if ai[j]<ai[i]:
            ans[i]=max(ans[j]+1,ans[i])
print(max(ans))            



    

