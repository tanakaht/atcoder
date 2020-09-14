N = int(input())
L = sorted(list(map(int, input().split())))
ans = 0
for l1 in L:
    for l2 in L:
        for l3 in L:
            ans += (l1 !=l2) and (l2 != l3) and (l3 != l1) and (2*max(l1, l2, l3) < l1+l2+l3)
print(ans//6)
