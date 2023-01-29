def fibonacci(n):
    zero=[1,0,1]
    one=[0,1,1]
    if 2 < n:
        for i in range(2, n):
            zero.append(zero[i-1] + zero[i])
            one.append(one[i-1] + one[i])
    print(f"{zero[n]} {one[n]}")
 
N = int(input())
for _ in range(N):
    n = int(input())
    fibonacci(n)
