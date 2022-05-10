n,w,l=map(int, input().split())
t=list(map(int, input().split()))

b=[0]*w
time =0

while t:
    time+=1 
    b.pop(0)
    if sum(b)+t[0]<=l:
            b.append(t[0])
            t.pop()
            
            
    else:
         b.append(0)
            
time+=w
print(time)              




            


