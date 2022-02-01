a = input()
b = input()
c = input()

# xの何文字目から被せてしまって良いか
def get_from_idx(x, y):
    ret = []
    for i in range(len(x)):
        j = 0
        while i+j<len(x) and j<len(y) and (x[i+j]==y[j] or x[i+j]=='?' or y[j]=='?'):
            j += 1
        if i+j==len(x) or j==len(y):
            ret.append(i)
    ret.append(len(x))
    return ret

N = len(a)+len(b)+len(c)
ans = N
for x, y, z in [[a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]]:
    idxs_xy = get_from_idx(x, y)
    idxs_xz = set(get_from_idx(x, z))
    idxs_yz = get_from_idx(y, z)
    # ptn1
    n2 = len(idxs_yz)-1
    for n1 in range(len(idxs_xy)):
        while n2 > 0 and idxs_xy[n1]+idxs_yz[n2-1]>=len(x):
            n2 -= 1
        if idxs_xy[n1]+idxs_yz[n2]>=len(x):
            ans = min(ans, max(len(x), idxs_xy[n1]+max(len(y), idxs_yz[n2]+len(z))))
        else:
            ans = min(ans, len(x)+len(z))
    # ptn2
    n2 = len(idxs_yz)-1
    for n1 in range(len(idxs_xy)):
        for n2 in range(len(idxs_yz)):
            if idxs_xy[n1]+idxs_yz[n2] in idxs_xz:
                ans = min(ans, max(len(x), idxs_xy[n1]+max(len(y), idxs_yz[n2]+len(z))))
    # ptn3
    for v3 in idxs_xz:
        if idxs_xy[0]+len(y)<=v3:
            ans = min(ans, max(len(x), v3+len(z)))

print(ans)
