#원생들이 한 조일때 티 비용에서 큰 비용대로 n-k개 뺌
import sys
n,k=map(int, sys.stdin.readline().split())
tall=list(map(int,sys.stdin.readline().split()))

tee=[]
for i in range(n-1):
    tee.append(tall[i+1]-tall[i])

tee.sort()
print(sum(tee[:n-k]))

 # 시간초과
''''   
tee.sort(reverse=True) #정렬해서 뺌  
    
for i in range(n-k):
    del tee[i]
'''    



