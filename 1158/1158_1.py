n,k=map(int,input().split())

ans=[]
arr=[i for i in range(1,n+1)]
num=k-1

for i in range(n):
    if len(arr)>num:
        ans.append(arr.pop(num))
        num+=k-1
    else:
        num=num%len(arr)
        ans.append(arr.pop(num))
        num+=k-1    
#참고        
print("<",", ".join(str(i) for i in ans),">",sep="")        
