import math

def ceil(num, den):
    return -(-num//den)

N, L, W = map(int, input().split())
A = list(map(int, input().split()))
A.append(L)
A = sorted(A)
ans = 0
bef = -W
for a in A:
    ans += max(0, ceil(a-(bef+W), W))
    bef = a
print(ans)
