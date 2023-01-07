from sys import stdin
input=stdin.readline
N = int(input().rstrip())
nums = list(map(int,input().split()))
idx_s=[0]
answer=[-1 for _ in range(N)]
for idx in range(1,N):
  if len(idx_s)==0:
    idx_s.append(idx)
  elif nums[idx] <= nums[idx_s[-1]]:
    idx_s.append(idx)
  else:
    max=nums[idx]
    while len(idx_s)>0 and nums[idx_s[-1]] < max:
      answer[idx_s.pop()] = max
    idx_s.append(idx)
print(*answer)