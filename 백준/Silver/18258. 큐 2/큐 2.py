import sys

n = int(sys.stdin.readline())
q = []
#i = [0 1 2 3 4]
#q = [1 2 3 4 5]
idx=0
for _ in range(n):
  order = list(sys.stdin.readline().split())
  if order[0]=='push':
    q.append(int(order[1]))
  elif order[0]=='size':
    print(len(q)-idx)
  elif order[0]=='empty':
    if idx != len(q):
      print(0)
    else:
      print(1)
  elif len(q)-idx == 0: # 비어있으면
    print(-1)
  elif order[0]=='pop':
    print(q[idx])
    idx+=1
  elif order[0]=='front':
    print(q[idx])
  elif order[0]=='back':
    print(q[-1])   