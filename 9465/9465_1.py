t=int(input())

for i in range(t):
    arr=[]
    n=int(input())
    for j in range(2):
        score=list(map(int,input().split()))
        arr.append(score)
    for k in range(1,n):
        if k==1:
            arr[0][1]+=arr[1][0] 
            arr[1][1]+=arr[0][0]
        else:
            arr[0][k]+=max(arr[1][k-1],arr[1][k-2])
            arr[1][k]+=max(arr[0][k-1],arr[0][k-2])
    print(max(arr[0][n-1],arr[1][n-1]))                   
