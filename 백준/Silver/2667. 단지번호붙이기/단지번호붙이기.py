def bfs(r,c,cnt):
  a[r][c]=0
  cnt+=1
  if r<N-1 and a[r+1][c]==1:cnt = bfs(r+1,c,cnt)
  if c<N-1 and a[r][c+1]==1:cnt = bfs(r,c+1,cnt)
  if 0<r and a[r-1][c]==1:cnt = bfs(r-1,c,cnt)
  if 0<c and a[r][c-1]==1:cnt = bfs(r,c-1,cnt)
  return cnt
N = int(input())
a=[]
num_cnt=cnt=0
num=[]
for i in range(N):
  a.append(list(map(int,input())))
for r in range(N):
  for c in range(N):
    if a[r][c]==1:
      num_cnt+=1
      num.append(bfs(r,c,cnt))
      cnt=0
print(num_cnt)
for n in sorted(num):
  print(n)