# 참고

num='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=''
n,b=map(int,input().split())

while n:
    ans=num[n%b]+ans
    n=n//b
print(ans)    