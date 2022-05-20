n=int(input())
num=list(map(int,input().split()))

sosu=0

for i in num:
    for j in range(2,i+1):
        if i%j==0:
            if i==j:
                sosu+=1
            break        
                
print(sosu)                

