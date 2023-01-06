#from collections import deque
exp=list(input())
exp.append('.')
tmp=sum=0
ck=0 # 기본은 +, 1이면 -
for c in exp:
  if c.isdecimal():
    tmp *= 10
    tmp += int(c)
  elif ck==1:
      sum = sum-tmp
      tmp = 0
  else:
    sum = sum + tmp
    tmp = 0
    if c == '-':
      ck=1
print(sum)