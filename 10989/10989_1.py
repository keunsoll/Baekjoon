import sys
input=sys.stdin.readline

n=int(input())
numList=[]

for i in range(n):
    numList.append(int(input()))

ans=sorted(numList)
for i in ans:
    print(i)
    