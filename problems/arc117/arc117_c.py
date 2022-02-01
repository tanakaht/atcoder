N = int(input())
d = {'B': 0, 'W':1, 'R': 2}
C = [d[c] for c in input()]
P = 3

ans = 0
hugou = pow(-1, N-1)
nume_cnt = [0, 1, 0]
deno_cnt = [0, 1, 0]
for i, c in enumerate(C):
    if nume_cnt[0] > deno_cnt[0]:
        ans = ans
    else:
        comb_ = pow(2, (nume_cnt[2]+deno_cnt[2])%2, P)
        ans = (ans+hugou*comb_*c)%P
    nume = N-(i+1)
    deno = i+1
    while nume and nume%3==0:
        nume //= 3
        nume_cnt[0] += 1
    nume_cnt[nume%3] += 1
    while deno and deno%3==0:
        deno//=3
        deno_cnt[0] += 1
    deno_cnt[deno%3] += 1


print('BWR'[ans])
