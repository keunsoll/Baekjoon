n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))
ans=sorted(num)
for i in range(len(num)):
    print(ans[i])    

