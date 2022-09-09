
l,p=map(int,input().split())

n=list(map(int,input().split()))

p=l*p
for i in n:
    print(i-p,end=" ")


