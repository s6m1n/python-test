n = list(map(int,input().split()))
s = set(n)
if len(s)==1:
  print(10000+s.pop()*1000)
elif len(s)==3:
  print(max(n)*100)
else:
  n.remove(s.pop())
  n.remove(s.pop())
  print(1000+n[0]*100)