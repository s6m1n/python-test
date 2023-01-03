import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
n=list(map(int,input().split()))
[n.append(num) for num in lst if num==n[0]]
print(len(n)-1)