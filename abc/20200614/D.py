N = int(input())
A = list(map(int, input().split()))
maxA = max(A)
counter = [0]*(maxA+1)
for ai in A:
    for m in range(ai, maxA+1, ai):
        counter[m] += 1
ans = 0
for ai in A:
    ans += (counter[ai] == 1)
print(ans)
