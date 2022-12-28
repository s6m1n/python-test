import sys
n=int(sys.stdin.readline())
s=[]

for _ in range(n):
  order = sys.stdin.readline().split()
  ord = order[0]
  if ord == 'push':
    s.append(int(order[1]))
  elif ord == 'pop':
    if len(s)==0:
      print(-1)
    else:
      a=s.pop()
      print(a)

  elif ord == 'size':
    print(len(s))

  elif ord == 'empty':
    if len(s)==0:
      print(1)
    else:
      print(0)
  
  elif ord == 'top':
    if len(s)>0:
      print(s[-1])
    else:
      print(-1)