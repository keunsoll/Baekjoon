n=int(input())
a=list(map(int, input().split()))

stack=[]
ans=[-1]*n

for  i in range(n):
    while stack and a[stack[-1]]<a[i]:
        ans[stack.pop()]=a[i]
    stack.append(i)   

for i in ans:
    print(i, end=" ")    
        


