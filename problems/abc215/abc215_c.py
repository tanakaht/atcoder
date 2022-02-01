import itertools
S, K = input().split()
K = int(K)
P = set(["".join(s) for s in itertools.permutations(S, len(S))])
print(sorted(P)[K-1])
