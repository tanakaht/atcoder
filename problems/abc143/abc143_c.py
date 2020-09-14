N = int(input())
S = input()


ans = 0
pre = None
for s in S:
    ans += (pre != s)
    pre = s
print(ans)
