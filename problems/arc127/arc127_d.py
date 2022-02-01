import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
As0, Bs0, As1, Bs1 = [0]*18, [0]*18, [0]*18, [0]*18
AB = sorted(zip(A, B), key=lambda x: x[0]^x[1])[::-1]
def process(a, b, pre_idx, new_idx):
    if pre_idx==-1 or a&(1<<pre_idx):
        for i in range(18):
            As0[i] -= (a&(1<<i))
            As1[i] -= ((~a)&(1<<i))
    else:
        for i in range(18):
            Bs0[i] -= (b&(1<<i))
            Bs1[i] -= ((~b)&(1<<i))
    if new_idx==-1 or a&(1<<new_idx):
        for i in range(18):
            As0[i] += (a&(1<<i))
            As1[i] += ((~a)&(1<<i))
    else:
        for i in range(18):
            Bs0[i] += (b&(1<<i))
            Bs1[i] += ((~b)&(1<<i))

ans = 0
idxs = [-1]*N
for i in range(N):
    a, b = AB[i]
    j = i-1
    while j>=0 and ((a^b)^(A[j]^B[j])).bit_length()-1 > idxs[j]:
        a_, b_ = AB[j]
        pre_idx = idxs[j]
        new_idx = (a^b^a_^b_).bit_length()-1
        process(a_, b_, pre_idx, new_idx)
        idxs[j] = new_idx
        j -= 1
    for j in range(18):
        if (a>>j)&1:
            ans += As1[j]
        else:
            ans += As0[j]
        if (b>>j)&1:
            ans += Bs1[j]
        else:
            ans += Bs0[j]
    for i in range(18):
        As0[i] += (a&(1<<i))
        As1[i] += ((~a)&(1<<i))
    print(idxs)
print(AB)
print(ans)
