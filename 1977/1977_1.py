m=int(input())
n=int(input())

arr=[]
for i in range(m,n+1):
    if i==(int(i**0.5))**2:
        arr.append(i)
if len(arr)==0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])