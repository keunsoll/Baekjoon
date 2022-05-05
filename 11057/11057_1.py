n=int(input())

a=[[0]*10 for i in range(1001)]
a[1]=[1]*10
    
for i in range(2,n+1):
    a[i][0]=1
    for j in range(10):
        a[i][j]=a[i-1][j] + a[i][j-1]
print(sum(a[n])%10007)