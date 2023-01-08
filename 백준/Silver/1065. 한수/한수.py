N=int(input())
s=[]
cnt=0
for i in range(1,N+1):
  ck=1
  while i>0:
    s.append(int(i%10))
    i=int(i/10)
  tmp=s.pop()
  if s:
    sub=tmp-s[-1]
    while s:
      tmp=s.pop()
      if not s:
        break
      elif tmp-s[-1]!=sub:
        ck=0
        break
  if ck==1:
    cnt+=1
  s=[]
print(cnt)