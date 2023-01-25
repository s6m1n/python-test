def bfs(n):
  visited[n]=1
  for i in range(1,N+1):
    if matrix[n][i]==1 and visited[i]==0:
      bfs(i)
N = int(input())
M = int(input())
visited=[0]*(N+1)
matrix=[[0 for _ in range(N+1)] for _ in range(N+1)]
for m in range(M):
  a,b=list(map(int,input().split()))
  matrix[a][b]=matrix[b][a]=1
bfs(1)
print(visited.count(1)-1)