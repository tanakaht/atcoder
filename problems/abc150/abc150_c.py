from itertools import permutations

N = int(input())
P = ''.join(input().split())
Q = ''.join(input().split())

l = sorted(permutations(range(1, N + 1), N))
d = {''.join(map(str, k)): v+1 for v, k in enumerate(l)}
print(abs(d[P]-d[Q]))
