N, B = map(int, input().split())
numes = [2, 3, 4, 5, 6, 7, 8, 9]
def f(x):
    ret = 1
    while x:
        ret *= x%10
        x//=10
    return ret

cnt = 0
q = [(1, 0)] # numeがiでjこめから始める
ans = 0
ans += f(B)==0
while q:
    nume, j = q.pop()
    if j>=len(numes):
        continue
    ans += f(nume+B)==nume
    tmp = 1
    while B+nume*tmp <= N+1:
        q.append((nume*tmp, j+1))
        tmp *= numes[j]

print(ans)
