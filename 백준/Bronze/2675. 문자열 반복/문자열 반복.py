N=int(input())
for n in range(N):
  M, str=input().split()
  for s in str:
      print(s*int(M), end='')
  print()