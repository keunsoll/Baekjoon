m=int(input())
n=int(input())

arr=[]
for i in range(m,n+1):
    for j in range(2,i+1):
        if j==i:
            arr.append(i)
        elif i%j==0:
            break
if len(arr)==0:
    print(-1) 
else:
    print(sum(arr))
    print(arr[0])
                   
    
        
    