import collections

N = int(input())
A = list(map(int, input().split()))
c = collections.Counter(A)
base_ans = 0
for i in c.values():
    base_ans += (i)*(i-1)//2
for a in A:
    i = c[a]
    diff_ans = max(0, i-1)
    print(base_ans - diff_ans)
