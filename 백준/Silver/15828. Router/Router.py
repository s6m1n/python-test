from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
size=0
while 1:
  num = int(input())
  if num==0:
    q.popleft()    
    size-=1
  elif num==-1:
    break
  else: 
    if size<n:
      q.append(num)
      size+=1

if not q:
  print('empty')
else:
  print(*q)
#q.popleft() -> 큐 방향으로 데이터 빼기
#print(*q) -> 한 줄 출력