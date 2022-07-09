n=int(input())
dic={}

for i in range(n):
    card=int(input())
    if card in dic:
        dic[card]+=1
    else:
        dic[card]=1

ans=sorted(dic.items(),key=lambda x:(-x[1],x[0]))   
print(ans[0][0]) 
