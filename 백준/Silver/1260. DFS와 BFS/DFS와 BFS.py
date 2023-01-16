import sys
input = sys.stdin.readline

N,M,V = list(map(int,input().split()))
graph = [[0]*(N+1)  for i in range(N+1)]
visited = [0]*(N+1)

for m in range(M):
  a,b=list(map(int,input().split()))
  graph[a][b]=graph[b][a]=1

def dfs(v):
  visited[v]=1
  print(v,end=' ')
  for idx in range(1,N+1):
    if graph[v][idx] == 1 and visited[idx]==0:
      dfs(idx)
      
def bfs(v):
  visited[v]=0
  q = [v]
  while q:
    tmp = q.pop(0)
    print(tmp, end=' ')
    for idx in range(1, N+1):
      if visited[idx]==1 and graph[tmp][idx]==1:
        q.append(idx)
        visited[idx]=0
    
  
dfs(V)
print()
bfs(V)