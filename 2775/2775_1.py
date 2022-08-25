t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    p=[i for i in range(1,n+1)]

    for j in range(k):
        for k in range(1,n):
            p[k]+=p[k-1]
    print(p[-1])        