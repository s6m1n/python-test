N, K = map(int, input().split())
q = []
answer = []
[q.append(i) for i in range(1,N+1)]
while q:
  for _ in range(K-1):
    q.append(q.pop(0))
  answer.append(q.pop(0))
print(f'<{str(answer)[1:-1]}>')