N = int(input())
V = sorted(list(map(int, input().split())))[::-1]
ans = 0
deno = 2
for v in V:
    ans += v / deno
    deno *= 2
ans += V[-1] / deno * 2
print(ans)
