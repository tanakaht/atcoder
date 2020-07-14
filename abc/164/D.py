S = input()
modps = sorted([0]+[int(S[-i:])%2019 for i in range(1, len(S)+1)])
ans = 0
pre = -1
pre_cnt = 0
for modp in modps:
    if modp != pre:
        pre = modp
        pre_cnt = 1
    else:
        ans += pre_cnt
        pre_cnt += 1
print(ans)
