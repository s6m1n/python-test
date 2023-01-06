n=int(input()) #명 수
cnt=0
for t in sorted(list(map(int,input().split()))):cnt+=t*n;n-=1
print(cnt)