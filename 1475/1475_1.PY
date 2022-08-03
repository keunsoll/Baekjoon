n=input()
num=[0 for j in range(10)]
for i in n:
    if i=='9' or i=='6':
        if num[6]==num[9]:
            num[6]+=1
        else:
            num[9]+=1
    else:
        num[int(i)]+=1   
print(max(num))                 