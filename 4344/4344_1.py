
n=int(input())

#average=0
#score_s=0
#r=0
for i in range(n):
    a_score= map(int, input().split( ))
    score=list(a_score)
    average=0
    score_s=0
    for i in range(1,len(score)):
        score_s += score[i]
    average= score_s / score[0]
    r=0
    for i in range(1,len(score)):
        if score[i]>average:
            r+=1      
    ratio=(r/score[0])*100
    
    print("%.3f"%ratio+"%")

