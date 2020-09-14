from collections import deque

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
score = dict(r=P, s=R, p=S)
ans = 0
q = deque()
for i in range(K):
    s = T[i]
    ans += score[s]
    q.append(s)
for i in range(K, N):
    s = T[i]
    s_pre_k = q.popleft()
    if s == s_pre_k:
        q.append('n')
    else:
        ans += score[s]
        q.append(s)
print(ans)
