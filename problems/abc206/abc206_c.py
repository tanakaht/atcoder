from collections import Counter
N = int(input())
A = list(map(int, input().split()))
c = Counter(A)
ans = 0
for c in c.values():
    ans += c*(N-c)
print(ans//2)
