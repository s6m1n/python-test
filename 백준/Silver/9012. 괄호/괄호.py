num = int(input())
for n in range(0, num):
  cnt=0
  a = input()
  for i in a:
    if i == '(':
      cnt+=1
    elif i == ')':
      cnt-=1
      if cnt<0:
        print('NO')
        break
  if cnt==0:
    print('YES')
  elif cnt>0:
    print('NO')