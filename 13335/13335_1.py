n,w,l=map(int, input().split())
t=list(map(int, input().split()))

b=[0 for i in range(w)]
time =0


while t:
    time+=1 
    b.pop(0)
    if len(b)<=w:
            if sum(b)+t[0]<=l:
                    b.append(t[0])
                    t.pop(0)
                    
                    
                   
            else:
                    b.append(0)  
                    print(b)  
'''         
while(True):
        time+=1
        if(b.pop(0)==last):
                break 
#by 예은
'''
time+=w
print(time)              
