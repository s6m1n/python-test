from sys import stdin
txt = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()
answer=[]
s=[]
cnt=0
ck=0
for t in txt:
  if t==bomb[cnt]:
    ck=1
    answer.append(t)
    cnt+=1
    if cnt==len(bomb): #bomb가 완성되면 스택에서 pop하고 cnt 초기화
      [answer.pop() for i in range(len(bomb))]
      if s: cnt=s.pop() # 처리할 이전 bomb가 남아있으면 시작
      else: ck=cnt=0 # 아니면 cnt와 ck 초기화
  elif ck==1 and t==bomb[0]: # 중간에 새로운 bomb가 시작되면 s에 저장
    s.append(cnt)
    answer.append(t)
    cnt=1
  else:
    s=[]
    cnt=ck=0
    answer.append(t)
if answer:
  answer = ''.join(answer)
  print(answer)
else:
  print('FRULA')