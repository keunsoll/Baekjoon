import sys
n,m=list(map(int,sys.stdin.readline().split()))


sosu=[]


for i in range(n,m+1):
    if i==1:
        continue
    elif i==2:
        sosu.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
             break
            elif j==i-1:
                sosu.append(i)
           
for i in sosu:
    print(i)     
                
## 시간초과