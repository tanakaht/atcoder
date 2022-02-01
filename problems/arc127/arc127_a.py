N = int(input())
def cnt(keta):
    v = int('1'*keta)
    ret = 0
    n = 1
    while n*v<=N:
        ret += n
        n *= 10
    ret -= max(0, n*(v+1)//10-N-1)
    return ret

ans = 0
for keta in range(1, len(str(N))+1):
    ans += cnt(keta)
print(ans)
