from sys import stdin
txt = stdin.readline().rstrip()
s=[-1 for i in range(26)]
for idx in range(len(txt)):
  if s[ord(txt[idx])-ord('a')]==-1:
    s[ord(txt[idx])-ord('a')]=idx
print(*s)