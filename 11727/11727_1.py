n=int(input())

a=[0]*1001
a[1]=1
a[2]=3

for i in range(3,n+1):
    if i%2==0:
        a[i]= a[i-1]*2 +1
    else:
        a[i]= a[i-1]*2 -1
print(a[n]%10007)        