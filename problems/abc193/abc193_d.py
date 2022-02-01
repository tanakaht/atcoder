from collections import Counter

K = int(input())
taka = list(map(int, input()[:-1]))
ao = list(map(int, input()[:-1]))
rest = {i: K for i in range(1, 10)}
def score(l):
    ret = 0
    c = Counter(l)
    for i in range(1, 10):
        ci = c[i]
        ret += pow(10, ci)*i
    return ret

for i in taka+ao:
    rest[i] -= 1

ans = 0
for taka_i in range(1, 10):
    for ao_i in range(1, 10):
        if rest[taka_i] == 0 or rest[ao_i]==0 or (taka_i==ao_i and rest[taka_i] <= 1):
            continue
        if score(taka+[taka_i]) > score(ao+[ao_i]):
            if taka_i == ao_i:
                ans += rest[taka_i]*(rest[ao_i]-1)
            else:
                ans += rest[taka_i]*rest[ao_i]
print(ans/((9*K-8)*(9*K-9)))
