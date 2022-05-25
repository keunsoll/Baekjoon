num=int(input())
n=list(map(int, input().split()))

m=max(n)
sum=0
for i in range(num):
    sum+=n[i]/m*100
avg=sum/num
print(avg)

