# 가능한 경우의 수를 다 만든 다음 들어온 수와 s, b가 다르면 제거하는 식으로 해결해야 함
N = int(input())
hubo=[]
answer=[]
for i in range(1, 10):
  for j in range(1, 10):
    for k in range(1, 10):
      if i!=j and j!=k and i!=k: #겹치는 게 없으면 저장
        hubo.append([i,j,k])
cnt_r = 0
for _ in range(N): # N번 반복
  nums, s, b=list(input().split())
  s=int(s)
  b=int(b)
  tmp=set()
  nums = list(map(int,nums)) # 주어진 수
  for example in hubo: # 남은 hubo의 모든 경우의 수 example에 대해 검사
    tmp=set()
    s_cnt=b_cnt=0 # 카운트 초기화
    for i in range(3): # 3자리에 대해 스트라이크 검사
      if example[i] == nums[i]: # 스트라이크면
        s_cnt+=1 # s카운트 증가
      else: # 아니면 set에 추가
        tmp.add(nums[i])
        tmp.add(example[i])
    if s_cnt == s and b == 6-(2*s_cnt+len(tmp)):
      answer.append(example)
      #hubo.remove(example) # 후보에서 example 제거
  hubo = answer
  answer=[]
print(len(hubo))