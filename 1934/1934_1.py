import sys
input=sys.stdin.readline
t=int(input())

for i in range(t):
    num=list(map(int,input().split()))
    for j in range(1,min(num)+1):
        if num[0]%j==0 and num[1]%j==0:
            a=j
    ans=num[0]*num[1]//a
    print(ans)        

