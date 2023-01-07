from sys import stdin
input = stdin.readline
N, X = list(map(int,input().split()))
A = list(map(int,input().split()))
[print(i,end=' ') for i in A if i < X]