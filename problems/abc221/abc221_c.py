N = input()
ans = -1
for bit in range(1<<len(N)):
    l, r = [], []
    for i in range(len(N)):
        if (bit>>i)&1:
            l.append(N[i])
        else:
            r.append(N[i])
    l, r = sorted(l)[::-1], sorted(r)[::-1]
    if len(l)==0 or len(r)==0 or l[0]==0 or r[0]==0:
        continue
    l, r = int("".join(l)), int("".join(r))
    ans = max(ans, l*r)
print(ans)
