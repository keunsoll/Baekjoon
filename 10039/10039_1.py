arr=[]
for i in range(5):
    score=int(input())
    if score<40:
        score=40
    arr.append(score)
   
ans=sum(arr)/5
print(int(ans))
