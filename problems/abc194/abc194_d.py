N = int(input())
ans = 0
for i in range(1, N):
    p = i/N
    ans += 1/(1-p)
print(ans)
