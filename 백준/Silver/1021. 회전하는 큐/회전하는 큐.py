import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
q = deque()
[q.append(i) for i in range(1,N+1)] # 오름차순 수가 담긴 큐
answer = list(map(int,input().split())) # 뽑으려는 수가 담긴 큐
i=0
cnt=0
while i<M:
  tar_idx = q.index(answer[i]) # q에서 tar_idx 잡기
  if tar_idx < len(q)/2:
    q.rotate(-1*tar_idx)
  # if answer[i]==q[0]: # 찾으면
  else:
    q.rotate(len(q)-tar_idx)
    tar_idx = len(q)-tar_idx
  q.popleft()
  cnt+=tar_idx
  i+=1
print(cnt)