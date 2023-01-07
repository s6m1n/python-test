from sys import stdin
input = stdin.readline
N = int(input())
people=[]
answer=[1 for i in range(N)]
for i in range(N):
  people.append(list(map(int,input().split())))
for i in range(N):
  cnt=idx=0
  while idx<N:
    if idx==i:
      idx+=1
      continue
    elif people[i][0]<people[idx][0] and people[i][1]<people[idx][1]:
      cnt+=1
    idx+=1
  answer[i]+=cnt
print(*answer)