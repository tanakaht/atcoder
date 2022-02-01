A, B, K = map(int, input().split())

def comb(n, r):
    if n < r or r < 0:
        return 0
    nume = 1
    deno = 1
    for i in range(1, r + 1):
        nume *= (n - i + 1)
        deno *= (i)
    return nume//deno

ans = ''
while A+B>0:
    if comb(A+B-1, A-1)>=K:
        ans += 'a'
        A -= 1
    else:
        ans += 'b'
        K -= comb(A+B-1, A-1)
        B -= 1
print(ans)
