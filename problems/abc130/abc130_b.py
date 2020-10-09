N, X = map(int, input().split())
L = list(map(int, input().split()))
ans = 0
tmp = 0
for l in L:
    ans += (tmp <= X)
    tmp += l
ans += (tmp <= X)
print(ans)
