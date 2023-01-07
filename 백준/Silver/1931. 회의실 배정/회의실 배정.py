from collections import deque
N = int(input())
d=[]
[d.append(list(map(int,input().split()))) for _ in range(N)]
#리스트에 수 저장
d=deque(sorted(d))
min = d.popleft()
answer=0
while d:
  tmp = d.popleft()
#  for i in range(start, N):
  if tmp[1]<min[1]:
    min=tmp
  elif min[1]<=tmp[0]: # 끝에 오면
    min=tmp
    answer+=1
print(answer+1)