import sys
input = sys.stdin.readline
N = int(input())
num=666
cnt=0
while 1:
  tmp = num
  ck=0
  while tmp>0:#자릿수 검사
    if int(tmp%10)==6:
      ck+=1
    else:
      ck=0
    if ck==3:
      cnt+=1
      break
    tmp = int(tmp/10)
  if cnt==N:
    print(num)
    break
  num+=1