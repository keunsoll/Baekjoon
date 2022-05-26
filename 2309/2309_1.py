n=[]
for i in range(9):
    n.append(int(input()))

tall=sum(n)
for i in range(8):
    for j in range(i+1,9):
        if tall-(n[i]+n[j])==100:
            no1=n[i]
            no2=n[j]

n.remove(no1)
n.remove(no2)
n.sort()
for i in n:
    print(i)
