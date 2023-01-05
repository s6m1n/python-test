n=int(input())
ck=0
start = n - 54
if start<0:
  start = 0
for i in range(start,n):
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
if ck == 0:
  print(0)