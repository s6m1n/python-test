l = list(map(int,input().split()))
a = [1,1,2,2,2,8]
l = [j-i for i,j in zip(l,a)]
print(*l)