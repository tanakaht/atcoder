import math
N = int(input())
A = list(map(int, input().split()))
entire_cnt = N*(N-1)//2 + N


class BIT:
    def __init__(self, len_A):
        self.N = len_A + 10
        self.bit = [0]*(len_A+10)

    # sum(A0 ~ Ai)
    # O(log N)
    def query(self, i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            idx -= idx & (-idx)
        return res

    # Ai += x
    # O(log N)
    def update(self, i, x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx & (-idx)


def is_ok(x):
    is_bigger = [2 * (a >= x) - 1 for a in A]  # sumが>=0の区間を数える=>転倒数
    cumsum = [0]*(N+1)
    for i in range(N):
        cumsum[i + 1] = cumsum[i] + is_bigger[i]
    bit = BIT(N + 1)
    cnt = 0
    order = {v: i for i, v in enumerate(sorted(cumsum))}
    # sorted(enumerate(cumsum), key=lambda x: x[1])
    for v in cumsum:  #sorted(enumerate(cumsum), key=lambda x: x[1]):
        i = order[v]
        cnt += bit.query(i)
        bit.update(i, 1)
    return cnt >= math.ceil(entire_cnt/2)


def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = bisect(pow(10, 9) + 1, 0)
print(ans)
