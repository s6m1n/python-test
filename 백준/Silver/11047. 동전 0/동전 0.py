N, M = list(map(int,input().split()))
l=[]
[l.append(int(input())) for _ in range(N)] 
l.sort(reverse = True)
cnt=0

for n in l:
  if M >= n:
    cnt += int(M/n)
    M = int(M%n)
print(cnt)