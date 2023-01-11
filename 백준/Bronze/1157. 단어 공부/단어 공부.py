str=input().upper()
dic={}
if len(str)==1:
  print(str)
else:
  for t in str:
    if t in dic:
      dic[t] += 1
    else:
      dic[t] = 0
  s = sorted(dic.items(), key=lambda dic: dic[1], reverse=True)
  if s[0][1]==s[1][1]:
    print('?')
  else:
    print(s[0][0])