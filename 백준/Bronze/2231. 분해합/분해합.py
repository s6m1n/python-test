n=int(input())
ck=0
for i in range(1,n):
  tmp = num = i
  while True :
    num+=int(i%10)
    i=int(i/10)
    if i==0:
      break
  if num == n:
    print(tmp)
    ck=1
    break
if ck==0:
  print(ck)