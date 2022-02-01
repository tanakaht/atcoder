N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
counts = {i: 0 for i in range(1, N+1)}
for c in C:
    counts[B[c-1]] += 1
ans = 0
for a in A:
    ans += counts[a]
print(ans)
