N = int(input())
S = input()
wcnt = S.count('W')
ecnt = 0
ans = N
for s in S:
    if s == 'W':
        wcnt -= 1
    ans = min(ans, N-wcnt-ecnt-1)
    if s == 'E':
        ecnt += 1
print(ans)
