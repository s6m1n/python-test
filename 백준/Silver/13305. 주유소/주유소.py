from collections import deque
N = int(input())
road = deque(map(int,input().split()))
city = deque(map(int,input().split()))
l = sorted(city)
sum = tmp = 0
now = city.popleft()
for c in city:
  sum += now*road.popleft()
  if now > c:
    now = c
print(sum)