
x=[]
y=[]
for i in range(3):
    a,b=list(map(int,input().split()))
    x.append(a)
    y.append(b)

#count 함수
for i in range(3):
    if x.count(x[i])==1:
        c=x[i]
    if y.count(y[i])==1:
        d=y[i]

print(c,d)
