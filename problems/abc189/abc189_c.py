import bisect
N = int(input())
A = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])
appeared = [-1, N]
ans = 0
for i, a in A:
    idx = bisect.bisect(appeared, i)
    ans = max(ans, (appeared[idx] - appeared[idx-1]-2+1)*a)
    appeared = appeared[:idx] + [i] + appeared[idx:]
print(ans)
