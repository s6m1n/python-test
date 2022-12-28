import sys
n = int(sys.stdin.readline())
s=[]
for _ in range(n):
  a = int(sys.stdin.readline())
  if a == 0:
    s.pop()
  else:
    s.append(a)
print(sum(s))