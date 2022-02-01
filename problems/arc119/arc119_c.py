from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cur = 0
Acum = [0]*(N+1)
for i in range(N):
    if i%2==0:
        Acum[i+1] = Acum[i]+A[i]
    else:
        Acum[i+1] = Acum[i]-A[i]

ans = 0
for cnt in Counter(Acum).values():
    ans += (cnt*(cnt-1))//2
print(ans)
