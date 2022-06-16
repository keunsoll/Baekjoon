h,w=map(int,input().split())
block=list(map(int,input().split()))

rainwater=0
for i in range(1,w-1):
    left_m=max(block[:i])
    right_m=max(block[i:])
    
    Min=min(left_m, right_m)
    if block[i]<Min:
        rainwater+=Min-block[i]
print(rainwater)        

    