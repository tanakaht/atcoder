from collections import defaultdict, deque
import sys

class BIT:
    def __init__(self,len_A):
        self.N = len_A + 10
        self.bit = [0]*(len_A+10)

    # sum(A0 ~ Ai)
    # O(log N)
    def query(self,i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            idx -= idx&(-idx)
        return res

    # Ai += x
    # O(log N)
    def update(self,i,x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx&(-idx)

    # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
    # O(log N)
    def lower_left(self,w):
        if (w < 0):
            return -1
        x = 0
        k = 1<<(self.N.bit_length()-1)
        while k > 0:
            if x+k < self.N and self.bit[x+k] < w:
                w -= self.bit[x+k]
                x += k
            k //= 2
        return x

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_ = [0]*N
B_ = [0]*N
for i in range(N):
    A_[i] = A[i]+i
    B_[i] = B[i]+i
d = defaultdict(deque)
for i in range(N):
    d[A_[i]].append(i)

deleted = BIT(N)
ans = 0
for i in range(N):
    b = B_[i]
    if not d[b]:
        print(-1)
        sys.exit(0)
    j = d[b].popleft()
    deleted.update(j+1, 1)
    ans += j-deleted.query(j)
print(ans)
