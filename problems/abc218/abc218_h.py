import sys
import heapq

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

    def get(self, i):
        return self.query(i)-self.query(i-1)


N, R = map(int, input().split())
A = list(map(int, input().split()))
R = min(R, N-R)
if N//2==R:
    print(sum(A))
    sys.exit(0)
available = BIT(N)
for i in range(N):
    available.update(i, 1)
q = []
for i in range(N-2):
    q.append((-(A[i]+A[i+1]), i))
heapq.heapify(q)
ans = 0
for _ in range(R):
    while q:
        v, i = heapq.heappop(q)
        v *= -1
        cnt = available.query(i)
        j = available.lower_left(cnt+1)
        if (not available.get(i)) or j>=N-1 or v!=A[i]+A[j]:
            continue
        available.update(i, -1)
        available.update(j, -1)
        ans += v
        if cnt >= 2:
            l, r = available.lower_left(cnt-1), available.lower_left(cnt)
            if r<N-1:
                heapq.heappush(q, (-(A[l]+A[r]), l))
        break


print(ans)
