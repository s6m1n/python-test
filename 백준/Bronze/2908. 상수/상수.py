N=list(input().split())
n=[]
n.append(int(N[0][::-1]))
n.append(int(N[1][::-1]))
print(max(n))