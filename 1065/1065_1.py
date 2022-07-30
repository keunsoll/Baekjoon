n=int(input())

ans=0
for i in range(1,n+1):
    if i<100:
        ans+=1
    else:
        num=list(map(int,str(i)))
        if num[1]-num[0]==num[2]-num[1]:
            ans+=1   
print(ans)            
