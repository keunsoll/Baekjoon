import sys
n=int(sys.stdin.readline())

mmax=[0 for i in range(3)]
mmin=[0 for i in range(3)]

maxx=[0 for i in range(3)]
minn=[0 for i in range(3)]

for i in range(n):
    num=list(map(int,sys.stdin.readline().split()))
    for j in range(3):
        if j==0:
            mmax[j]=num[j]+max(maxx[j],maxx[j+1])
            mmin[j]=num[j]+min(minn[j],minn[j+1])
        if j==1:
            mmax[j]=num[j]+max(maxx[j-1],maxx[j],maxx[j+1])
            mmin[j]=num[j]+min(minn[j-1],minn[j],minn[j+1])  
        if j==2:
            mmax[j]=num[j]+max(maxx[j-1],maxx[j])
            mmin[j]=num[j]+min(minn[j-1],minn[j]) 
    for k in range(3):
        maxx[k]=mmax[k]
        minn[k]=mmin[k]

print(max(maxx), min(minn))

