# 참고
from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
c=deque([i for i in range(1,n+1)])
print('<',end='')

while c:
    for i in range(k-1):
        c.append(c[0])
        c.popleft()
    print(c.popleft(),end='')
    if c:
        print(', ', end='')
print('>')        

