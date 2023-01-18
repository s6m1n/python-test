def fact(n):
    ans = 1
    if 0<n :
        ans = n * fact(n-1)
    return ans
n = int(input())
print(fact(n))