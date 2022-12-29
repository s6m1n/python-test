import sys
while 1 :
  txt = sys.stdin.readline().rstrip() # 왜 하는지 찾아봐(개행문자?)
  if txt=='.':
    break
  s=[]
  ck=0
  for c in txt:
    if c=='(' or c=='[':
      s.append(c)
    if c==')' or c==']':
      if not s: #스택이 비어있다면
        ck=1
        break
      elif c==')' and s[-1]=='(': # 맞는 짝이라면
        s.pop()
      elif c==']' and s[-1]=='[': # 맞는 짝이라면
        s.pop()
      else:
        ck=1
        break
    elif c=='.' and s:
        ck=1
        break
  if ck==1:
    print("no")
  else:
    print("yes")