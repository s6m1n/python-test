n=int(input())
for _ in range(n):
  N,M = list(map(int,input().split()))
  Mtmp=M
  Ntmp=N
  MNtmp=(M-N)
  Mpac=1
  Npac=1
  MNpac=1
  while Mtmp>1:
    Mpac=Mpac*Mtmp
    Mtmp-=1
    if Ntmp>1:
      Npac=Npac*Ntmp
      Ntmp-=1
    if MNtmp>1:
      MNpac=MNpac*MNtmp
      MNtmp-=1
  print(int(Mpac/(Npac*MNpac)))
  