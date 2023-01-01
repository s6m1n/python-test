n=float(input())
s = list(map(int,(input().split())))
M=max(s)
print(sum([i/M*100 for i in s])/n)