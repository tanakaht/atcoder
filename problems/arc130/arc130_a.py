N = int(input())
S = input()
ans = 0
pre = None
cnt = 0
for s in S:
    if pre==s:
        cnt += 1
    else:
        pre = s
        ans += cnt*(cnt-1)//2
        cnt = 1
ans += cnt*(cnt-1)//2
print(ans)
