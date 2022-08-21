n=int(input())

li=1
while n>li:
    n-=li
    li+=1
if li %2==0:
    up=n
    down=li-n+1
else:
    up=li-n+1
    down=n

print(up,down,sep="/")        
