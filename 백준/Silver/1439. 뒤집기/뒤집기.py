n=input()
cnt=0
num=n[0]
for idx in range(0,len(n)-1):
  if n[idx]!=n[idx+1] and n[idx+1]!=num:
    cnt+=1
print(cnt)
