import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
for _ in range(n):
  order = list(input().rstrip())
  m=int(input())
  l = list(input().strip()[1:-1].split(','))
  if m==0:
    q = deque()
  else:
    q = deque(l)
  l=[]
  r_cnt=0
  ck=0
  for ord in order:
    if ord=='R':
      r_cnt += 1
    elif len(q) != 0 and ord=='D':
      if r_cnt%2==1:
        q.pop()
      else:
        r_cnt=0
        q.popleft()
    else:
      ck=1
      break
  if ck==1:
    print('error')
  elif r_cnt%2==1:
    [l.append(q.pop()) for _ in range(len(q))]
    print("[" + ",".join(l) + "]")
  else:
    print("[" + ",".join(q) + "]")
