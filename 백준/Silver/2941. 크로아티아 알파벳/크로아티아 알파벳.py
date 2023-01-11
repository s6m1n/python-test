str=input()
cnt=len(str)
cnt -= str.count('dz=')*2
str=str.replace('dz=',' ')
cnt -= (str.count('c=')+str.count('c-')+str.count('d-')+str.count('lj')+str.count('nj')+str.count('s=')+str.count('z='))
print(cnt)