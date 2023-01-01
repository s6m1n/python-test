import sys
input = sys.stdin.readline
i = int(input())
for _ in range(i):
  cnt=0
  nums = list(map(int, input().split()))
  n = nums.pop(0)
  avg = float(sum(nums))/n
  for i in nums:
   if i > avg:
     cnt+=1
  print('{:.3f}%'.format(cnt/n*100,3))