import sys
input = sys.stdin.readline
cnt=N=int(input())
for i in range(N):
  s=[]
  word=input().rstrip()
  tmp=word[0]
  for t in word:
    if t not in s:
      s.append(t)
    elif t in s and tmp!=t:
      cnt-=1
      break
    tmp=t
print(cnt)