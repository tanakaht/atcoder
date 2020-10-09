from math import gcd

N = int(input())
A = list(map(int, input().split()))
gcd_all = A[0]
gcd_miss_one = set([A[1]])
for a in A[1:]:
    gcd_miss_one_new = set()
    for gcd_ in gcd_miss_one:
        gcd_miss_one_new.add(gcd(a, gcd_))
    gcd_miss_one = gcd_miss_one_new
    gcd_miss_one.add(gcd_all)
    gcd_all = gcd(a, gcd_all)
print(max(gcd_miss_one))
