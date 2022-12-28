import sys
n = int(sys.stdin.readline())
lst=[]
[lst.append(int(sys.stdin.readline())) for i in range(n)]

check=0
answer = []
s = [0]
tmp = 1

for num in lst:
  if num < s[-1]:
    check=1
    break
  elif s[-1] == num: # 스택에 있는지 확인, 있다면 pop 수행
    s.pop()
    answer.append('-')
  elif tmp <= n: # 스택에 없다면 tmp에서 확인, 작거나 같을 때
    while(tmp <= num):
      answer.append('+')
      if tmp < num: #tmp가 num보다 작으면
        s.append(tmp) # push하고
      else: # 같으면
        answer.append('-') # pop
      tmp+=1 # 다음 tmp로 이동
  else:
    check=1
    break

if check==0:
  [print(i) for i in answer]
else:
  print('NO')