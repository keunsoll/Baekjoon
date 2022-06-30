a,b=map(int,input().split())
aa,bb=a,b
# 유클리드 알고리즘
while bb!=0:
    aa=aa%bb
    aa,bb=bb,aa

print(aa)
print(a*b//aa)   