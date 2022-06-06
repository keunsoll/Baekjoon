n=int(input())

for i in range(n):
    ans=input()
    ansl=list(ans)
    sum=0
    count=0
    for i in ansl:
        if i=='O':
            count+=1
            sum+=count
            
        else:
            count=0
    print(sum)            
