n=int(input()) #명 수
time = list(map(int,input().split())) #시간 리스트
time.sort()
cnt=0
for t in time:
  cnt+=t*n
  n-=1
print(cnt)