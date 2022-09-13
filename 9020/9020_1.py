
num=list(range(2,10000))                 
prime_num=[]

def prime(n):
    if n<2:
        return False
    elif n==2:
        return True    
        
    else:
        for i in range(2,n): 
            if n%i==0: 
                return False     
        return True
    
            
for i in num:
    if prime(i):
        prime_num.append(i)


t=int(input())

for i in range(t):
    n=int(input())
    b=n//2
    for j in range(b,1,-1):
        if (j in prime_num) and (n-j in prime_num):
                print(j,n-j)
                break
                        
     