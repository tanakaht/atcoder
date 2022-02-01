import sys
N, K = map(int, input().split())
K -= 1
def get_sum_cnt(A):
    fr_, to_ = max(1, A-2*N), min(A-2, N)
    n = to_-fr_+1
    ret = n
    if A-to_-1>=N:
        ret += N*n
    elif A-fr_-1<N:
        ret += n*(2*A-(to_+fr_)-2)//2
    else:
        k = A-1-N
        ret += N*(k-fr_)
        ret += (to_-k+1)*(2*A-(k+to_)-2)//2

    if A-to_-N>=1:
        ret -= n*(2*A-(to_+fr_)-2*N)//2
    elif A-fr_-N<=1:
        ret -= n
    else:
        k = A-1-N
        ret -= (to_-k)
        ret -= (k-fr_+1)*(2*A-(k+fr_)-2*N)//2
    return ret

def sumijk_naive(A):
    ret = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            ret += 1<=A-i-j<=N
    return ret


sumijk = 3
while get_sum_cnt(sumijk) <= K:
    K -= get_sum_cnt(sumijk)
    sumijk += 1
i = max(1, sumijk-2*N)
def get_i_cnt(i):
    ret = min(N, sumijk-i-1)-max(1, sumijk-i-N)+1
    return ret
while get_i_cnt(i) <= K:
    K -= get_i_cnt(i)
    i += 1
j = max(1, sumijk-i-N)
while 1<K:
    K -= 1
    j+= 1
k = sumijk-i-j
for x in [i, j, k]:
    if not 1<=x<=N:
        raise ValueError
print(i, j, k)
print(i, j, k)
