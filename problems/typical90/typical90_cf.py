N = int(input())
S = input()
def cnt(l, r):
    n = r-l+1
    return n*(n+1)//2

ans = cnt(0, N-1)
l, r = 0, 0
while l<N:
    while r<N and S[l]==S[r]:
        r += 1
    ans -= cnt(l, r-1)
    l, r = r, r
print(ans)
