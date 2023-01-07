from sys import stdin
N = int(input())
people=[]
for i in range(N):
  people.append(list(map(int,stdin.readline().split())))
for i in range(N):
  answer=1
  idx=0
  while idx<N:
    if idx==i:
      idx+=1
      continue
    elif people[i][0]<people[idx][0] and people[i][1]<people[idx][1]:
      answer+=1
    idx+=1
  print(answer, end=' ')