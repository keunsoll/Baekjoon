num=[]
for i in range(9):
    a=int(input())
    num.append(a)

m=max(num)
w=num.index(m)+1
print(m)
print(w)    