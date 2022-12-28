a = list(input()) # 원래 list
s = [] # stack
cnt = 0 # 막대기 수

for i in range(len(a)):
  if a[i]=='(':
    s.append('(')
  else:
    if a[i-1]=='(': # 레이저면
      s.pop() # 레이저 제거
      cnt+=len(s) # 스택에 있는 괄호 수(막대기 수)만큼 추가
    else: # 막대기의 끝이면
      s.pop() # 막대기 제거
      cnt+=1 # 한 조각 추가
print(cnt)