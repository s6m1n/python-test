J=S=int(input())
j_s=s_s=0
stock=list(map(int,input().split()))
tmp=stock[0]
ck=0
for s in stock:
  if 0 < J//s: # 준현이가 살 수 있다면
    j_s += J//s # 산다
    J = int(J%s) # 사고 남은 돈
  if tmp < s: #주식이 올랐다면
    if 0<=ck: # 오르고 있으면
      ck+=1
      if 3<=ck: # 매도
        if 0 < s_s: # 팔 주식이 있으면
          S += s_s*s # cash%stock 판 돈 더해주기
          s_s = 0 # 전량 매도했으므로 0개
    else:ck=1 # 오르기 시작했을 때
  elif s < tmp: # 주식이 내리고있다면
    if ck<=0:
      ck-=1
      if ck<=-3: # 매수
        if 0 < S//s:
          s_s += S//s #cash//stock 산 주식 수만큼 덧셈
          S = int(S%s) # cash%stock 매수 후 남은 현금으로 교체
    else:ck=-1
  else:
    ck=0
  tmp=s
  
if stock[-1]*j_s+J > stock[-1]*s_s+S:
  print("BNP")
elif stock[-1]*j_s+J < stock[-1]*s_s+S:
  print("TIMING")
else:
  print("SAMESAME")