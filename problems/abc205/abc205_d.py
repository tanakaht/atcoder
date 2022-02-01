N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
cnt = 0
Qs = []
for i in range(Q):
    K = int(input())
    Qs.append((K, i))
Qs = sorted(Qs)
anss = [None]*Q
cnt = 0
for k, i in Qs:
    while cnt<N and A[cnt] <= k+cnt:
        cnt += 1
    anss[i] = k+cnt
print(*anss, sep='\n')
