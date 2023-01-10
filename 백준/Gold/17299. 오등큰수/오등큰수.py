from sys import stdin
N = int(stdin.readline().rstrip())
txt = stdin.readline().split()
answer = [-1 for i in range(N)]
dic=dict.fromkeys(txt,0)
for t in txt:
  dic[t] += 1
#dic value는 cnt
s=[] #idx 저장
min=1000000
for idx in range(0,N):
  if dic[txt[idx]]<=min: # 바로 전보다 같거나작은 애면 s에 추가
    s.append(idx)
    min=dic[txt[idx]]
  else:
    while s and dic[txt[s[-1]]] <= dic[txt[idx]]:
      answer[s.pop()]=int(txt[idx])
      if not s or dic[txt[idx]] <= dic[txt[s[-1]]]:
        min=dic[txt[idx]];s.append(idx);break
print(*answer)