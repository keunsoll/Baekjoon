d=int(input())
car=list(map(int,input().split()))

cnt=0

for i in range(len(car)):
    if car[i]==d:
        cnt+=1
print(cnt)        