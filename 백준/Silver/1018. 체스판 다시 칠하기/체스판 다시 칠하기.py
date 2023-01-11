import sys
input = sys.stdin.readline
N,M = list(map(int,input().split()))
chess=[]
answer=[]
for n in range(N):
  chess.append(input().rstrip())
cnt=[0,0] # 앞은 짝W 홀B, 뒤는 짝B 홀W
#WBWB / BWBW
for y_start in range(N-7):
  for x_start in range(M-7):
    for n in range(y_start,y_start+8):
      for m in range(x_start,x_start+8):
        if int(n+m)%2==0: # 짝수자리 검사
          if chess[n][m]=='B': #짝수자리 위치가 B색이면
            cnt[0]+=1
          else: #짝수자리 위치가 W색이면
            cnt[1]+=1
        else: # 홀수자리 검사
          if chess[n][m]=='B': #홀수자리 위치가 B색이면
            cnt[1]+=1
          else: #홀수자리 위치가 W색이면
            cnt[0]+=1
    answer.append(min(cnt))
    cnt=[0,0]
print(min(answer))