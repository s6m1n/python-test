N=int(input())
M=[]
str=[]
for n in range(N):
  i,j=input().split()
  M.append(int(i))
  str.append(j)
for n in range(N): 
  s=[t for t in str[n]]
  for idx in range(len(s)):
    for m in range(M[n]):
      print(s[idx], end='')
  print('')