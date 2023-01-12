import sys
sys.setrecursionlimit(10**7)

def dfs(start):
  visited[start] = 1
  next = arr[start]-1
  if visited[next] == 0:
    dfs(next)

N = int(input())
for n in range(N):
  cnt=0
  M = int(input())
  visited=[0]*M
  arr = list(map(int,input().split()))
  for m in range(0,M):
    if visited[m]==0:
      dfs(m)
      cnt+=1
  print(cnt)