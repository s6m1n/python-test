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

# for문 돌며 idx 한 칸씩 증가
# stack 검사하기
## 비어있으면 그냥 넣기
## s[-1]이랑 같거나 작으면 넣기, s[-1]보다 큰 애 나올 때까지 s.pop()하면서 값 바꿔주고 마지막에 자기 자신 append

# nums = list(map(int,input().split()))
# nums.reverse()
# answer=[]
# while nums:
#   N = nums.pop(); max = -1
#   for n in nums[::-1]:
#     if N<n: max = n; break
#   answer.append(max)
# print(*answer)

# 9 5 5 2 3 6 1 3 2 5  4  9  8  5  2
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# - 7 