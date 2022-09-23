from collections import deque

n,m,v=map(int,input().split())
visited=[0]*(n+1)
g=[[0]*(n+1) for i in range(n+1)]

def dfs(v):
    visited[v]=1
    print(v, end=" ")
    for i in range(1,n+1):
        if(visited[i]==0 and g[v][i]==1):
            dfs(i)

def bfs(v):
    q=deque([v])
    visited[v]=0
    while q:
        v=q.popleft()
        print(v,end=" ")
        for i in range(1,n+1):
            if visited[i]==1 and g[v][i]==1:
                q.append(i)
                visited[i]=0


for i in range(m):
    x,y=map(int,input().split())
    g[x][y]=g[y][x]=1

dfs(v)
print()
bfs(v)

    