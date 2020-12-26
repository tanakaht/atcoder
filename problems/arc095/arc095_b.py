N = int(input())
A = sorted(map(int, input().split()))
ai = A[-1]
ans = [-1, -1]
for a in A:
    r = min(a, ai - a)
    if r > ans[0]:
        ans = [r, a]
print(ai, ans[1])
