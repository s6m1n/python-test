import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
q = deque()
for _ in range(N):
  order = input().split()
  if order[0]=='push_front':
    q.appendleft(int(order[1]))
  elif order[0]=='push_back':
    q.append(int(order[1]))
  elif order[0]=='pop_front':
    if not q:
      print(-1)
    else:
      print(q.popleft())
  elif order[0]=='pop_back':
    if not q:
      print(-1)
    else:
      print(q.pop())
  elif order[0]=='size':
    print(len(q))
  elif order[0]=='empty':
    if not q:
      print(1)
    else:
      print(0)
  elif order[0]=='front':
    if not q:
      print(-1)
    else:
      print(q[0])
  elif order[0]=='back':
    if not q:
      print(-1)
    else:
      print(q[-1])